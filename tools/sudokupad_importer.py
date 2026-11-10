"""
SudokuPad puzzle importer.

Fetches a SudokuPad puzzle by URL or short ID, decodes
its 'scl' (zipped SCL JSON) or 'fpuz'/'fpuzzles'
payload, translates the recognized constraints into
this project's SudokuPuzzle API, and generates a Python
puzzle module plus an import report.

Unknown or ambiguous elements are never silently
ignored: they are listed in the report, and an import
is classified "Complete" only when every rule-bearing
element was recognized.

Usage:
    python -m tools.sudokupad_importer <url-or-id>
    python -m tools.sudokupad_importer <url-or-id> --module ctc_002
"""

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PUZZLE_API = "https://sudokupad.app/api/puzzle/{}"

SUPPORTED_SIZE = 9

EPSILON = 0.05


class SudokuPadImportError(Exception):
    """Raised when a puzzle cannot be fetched or decoded."""


# ----------------------------------------------------------
# LZ-string decompression (pure Python port of the
# reference lz-string decompressFromBase64).
# ----------------------------------------------------------

_KEY_B64 = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz0123456789+/="
)
_B64_INDEX = {c: i for i, c in enumerate(_KEY_B64)}


def decompress_from_base64(compressed):
    """Decompress an lz-string compressToBase64 payload."""
    if not compressed:
        return ""

    try:
        return _decompress(
            len(compressed), 32,
            lambda i: _B64_INDEX[compressed[i]],
        )
    except (KeyError, IndexError) as exc:
        raise SudokuPadImportError(
            "Invalid lz-string payload"
        ) from exc


def _decompress(length, reset_value, get_next_value):
    dictionary = {}
    enlarge_in = 4
    dict_size = 4
    num_bits = 3
    result = []

    state = {
        "val": get_next_value(0),
        "position": reset_value,
        "index": 1,
    }

    def read_bits(n):
        bits = 0
        power = 1
        maxpower = 1 << n

        while power != maxpower:
            resb = state["val"] & state["position"]
            state["position"] >>= 1

            if state["position"] == 0:
                state["position"] = reset_value
                state["val"] = get_next_value(state["index"])
                state["index"] += 1

            if resb > 0:
                bits |= power

            power <<= 1

        return bits

    first = read_bits(2)

    if first == 0:
        character = chr(read_bits(8))
    elif first == 1:
        character = chr(read_bits(16))
    else:
        return ""

    dictionary[3] = character
    w = character
    result.append(character)

    while True:
        if state["index"] > length:
            raise SudokuPadImportError(
                "Truncated lz-string payload"
            )

        code = read_bits(num_bits)

        if code == 0:
            dictionary[dict_size] = chr(read_bits(8))
            dict_size += 1
            code = dict_size - 1
            enlarge_in -= 1
        elif code == 1:
            dictionary[dict_size] = chr(read_bits(16))
            dict_size += 1
            code = dict_size - 1
            enlarge_in -= 1
        elif code == 2:
            return "".join(result)

        if enlarge_in == 0:
            enlarge_in = 1 << num_bits
            num_bits += 1

        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            entry = w + w[0]
        else:
            raise SudokuPadImportError(
                "Corrupt lz-string payload"
            )

        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        enlarge_in -= 1
        w = entry

        if enlarge_in == 0:
            enlarge_in = 1 << num_bits
            num_bits += 1


# ----------------------------------------------------------
# Parser for SudokuPad's "zipped" SCL JSON dialect:
# unquoted keys, single-quoted strings, bare tokens
# such as #0 / #F, and array elisions like [,,,].
# ----------------------------------------------------------

_BARE_TOKEN = re.compile(r"[A-Za-z0-9#_.+\-]+")
_NUMBER = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")

_ESCAPES = {
    "n": "\n", "t": "\t", "r": "\r",
    "'": "'", '"': '"', "\\": "\\", "/": "/",
}


class _JsParser:

    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self, message):
        return SudokuPadImportError(
            f"{message} at position {self.pos}"
        )

    def skip_ws(self):
        while (
            self.pos < len(self.text)
            and self.text[self.pos] in " \t\r\n"
        ):
            self.pos += 1

    def peek(self):
        if self.pos >= len(self.text):
            raise self.error("Unexpected end of data")

        return self.text[self.pos]

    def consume(self, expected):
        if self.peek() != expected:
            raise self.error(f"Expected {expected!r}")

        self.pos += 1

    def parse_value(self):
        self.skip_ws()
        char = self.peek()

        if char == "{":
            return self.parse_object()

        if char == "[":
            return self.parse_array()

        if char in "'\"":
            return self.parse_string(char)

        match = _NUMBER.match(self.text, self.pos)

        if match and match.group() not in ("-",):
            # Bare tokens such as 2a would also match a
            # number prefix; only accept the number when
            # the next character is a delimiter.
            end = match.end()

            if (
                end >= len(self.text)
                or self.text[end] in ",]}: \t\r\n"
            ):
                self.pos = end
                value = match.group()

                return (
                    float(value)
                    if "." in value or "e" in value.lower()
                    else int(value)
                )

        match = _BARE_TOKEN.match(self.text, self.pos)

        if not match:
            raise self.error(f"Unexpected character {char!r}")

        self.pos = match.end()
        token = match.group()

        if token == "true":
            return True

        if token == "false":
            return False

        if token in ("null", "undefined"):
            return None

        return token

    def parse_string(self, quote):
        self.consume(quote)
        parts = []

        while True:
            char = self.peek()
            self.pos += 1

            if char == quote:
                return "".join(parts)

            if char == "\\":
                escape = self.peek()
                self.pos += 1

                if escape == "u":
                    code = self.text[self.pos:self.pos + 4]
                    self.pos += 4
                    parts.append(chr(int(code, 16)))
                else:
                    parts.append(
                        _ESCAPES.get(escape, escape)
                    )
            else:
                parts.append(char)

    def parse_object(self):
        self.consume("{")
        result = {}

        self.skip_ws()

        if self.peek() == "}":
            self.pos += 1
            return result

        while True:
            self.skip_ws()
            char = self.peek()

            if char in "'\"":
                key = self.parse_string(char)
            else:
                match = _BARE_TOKEN.match(self.text, self.pos)

                if not match:
                    raise self.error("Expected object key")

                key = match.group()
                self.pos = match.end()

            self.skip_ws()
            self.consume(":")

            result[key] = self.parse_value()

            self.skip_ws()
            char = self.peek()

            if char == ",":
                self.pos += 1
                continue

            if char == "}":
                self.pos += 1
                return result

            raise self.error("Expected ',' or '}'")

    def parse_array(self):
        """
        Parse an array. Empty slots between commas are
        elisions and become None, so [,,] is three empty
        items in SudokuPad's zipped dialect.
        """
        self.consume("[")
        items = []

        self.skip_ws()

        if self.peek() == "]":
            self.pos += 1
            return items

        while True:
            self.skip_ws()
            char = self.peek()

            if char in ",]":
                items.append(None)
            else:
                items.append(self.parse_value())
                self.skip_ws()
                char = self.peek()

            if char == ",":
                self.pos += 1
                continue

            if char == "]":
                self.pos += 1
                return items

            raise self.error("Expected ',' or ']'")


def parse_zipped_json(text):
    """Parse SudokuPad's zipped SCL JSON dialect."""
    parser = _JsParser(text)
    value = parser.parse_value()
    parser.skip_ws()

    if parser.pos != len(text):
        raise SudokuPadImportError(
            "Trailing data after puzzle JSON"
        )

    return value


def normalize_color(value):
    """Expand zipped color shorthands such as #0 / #F."""
    if not isinstance(value, str) or not value.startswith("#"):
        return value

    digits = value[1:]

    if len(digits) == 1:
        digits = digits * 6
    elif len(digits) == 3:
        digits = "".join(c * 2 for c in digits)

    return "#" + digits.upper()


def _is_white(color):
    color = normalize_color(color) or ""
    return color.upper().startswith("#FFFFFF") and not (
        color.upper().endswith("00") and len(color) == 9
    )


def _is_black(color):
    color = normalize_color(color) or ""
    return color.upper().startswith("#000000") and not (
        color.upper().endswith("00") and len(color) == 9
    )


def _truthy_flag(value):
    """
    Interpret zipped boolean flags: PuzzleZipper
    shortens true/false to 't'/'f'.
    """
    if isinstance(value, str):
        return value.lower() in ("t", "true", "1")

    return bool(value)


# ----------------------------------------------------------
# Fetching and payload decoding
# ----------------------------------------------------------

_ID_PATTERN = re.compile(r"^[A-Za-z0-9]+$")

_DATA_PREFIXES = ("scl", "fpuzzles", "fpuz")


def extract_puzzle_reference(reference):
    """
    Interpret a CLI argument as encoded puzzle data,
    a SudokuPad URL, or a short puzzle ID.

    Returns ("data", payload) or ("id", puzzle_id).
    """
    reference = reference.strip()

    if any(
        reference.startswith(prefix)
        for prefix in _DATA_PREFIXES
    ) and len(reference) > 24:
        return "data", reference

    if "://" in reference or "sudokupad" in reference:
        path = reference.split("://")[-1]
        path = path.split("?")[0].rstrip("/")
        segment = path.split("/")[-1]

        if not segment:
            raise SudokuPadImportError(
                f"Could not find a puzzle ID in {reference!r}"
            )

        return extract_puzzle_reference(segment)

    if not _ID_PATTERN.match(reference):
        raise SudokuPadImportError(
            f"Invalid puzzle reference: {reference!r}"
        )

    return "id", reference


def fetch_payload(puzzle_id, timeout=30):
    """Fetch the encoded puzzle data for a short ID."""
    url = PUZZLE_API.format(puzzle_id)

    request = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(
            request, timeout=timeout
        ) as response:
            return response.read().decode("utf-8")

    except urllib.error.HTTPError as exc:
        raise SudokuPadImportError(
            f"SudokuPad returned HTTP {exc.code} for "
            f"puzzle {puzzle_id!r}"
        ) from exc

    except (urllib.error.URLError, OSError) as exc:
        raise SudokuPadImportError(
            f"Network error fetching puzzle "
            f"{puzzle_id!r}: {exc}"
        ) from exc


def decode_payload(payload):
    """
    Decode an encoded puzzle payload.

    Returns (format_name, data_dict) where format_name
    is "scl" or "fpuzzles".
    """
    payload = payload.strip()

    if payload.startswith("scl"):
        text = decompress_from_base64(payload[3:])

        if not text:
            raise SudokuPadImportError(
                "Empty scl payload after decompression"
            )

        return "scl", parse_zipped_json(text)

    for prefix in ("fpuzzles", "fpuz"):
        if payload.startswith(prefix):
            text = decompress_from_base64(
                payload[len(prefix):]
            )

            if not text:
                raise SudokuPadImportError(
                    "Empty fpuzzles payload after "
                    "decompression"
                )

            try:
                return "fpuzzles", json.loads(text)
            except json.JSONDecodeError as exc:
                raise SudokuPadImportError(
                    "Invalid fpuzzles JSON"
                ) from exc

    raise SudokuPadImportError(
        f"Unsupported puzzle encoding: "
        f"{payload[:12]!r}..."
    )


# ----------------------------------------------------------
# Geometry helpers
# ----------------------------------------------------------

def _near(value, target):
    return abs(value - target) < EPSILON


def _is_half(value):
    return _near(value % 1, 0.5)


def _is_whole(value):
    fraction = value % 1
    return fraction < EPSILON or fraction > 1 - EPSILON


def border_pair(center, size=SUPPORTED_SIZE):
    """
    Map a border-midpoint coordinate (row, column in
    SudokuPad float units) to the two adjacent cells.

    Returns ((cell_a, cell_b)) or None when the point
    is not on an interior cell border.
    """
    row, col = center

    if _is_whole(row) and _is_half(col):
        border = round(row)
        column = int(col)

        if 1 <= border <= size - 1 and 0 <= column < size:
            return (
                (border - 1, column),
                (border, column),
            )

    if _is_half(row) and _is_whole(col):
        border = round(col)
        line = int(row)

        if 1 <= border <= size - 1 and 0 <= line < size:
            return (
                (line, border - 1),
                (line, border),
            )

    return None


def chevron_inequality(waypoints, size=SUPPORTED_SIZE):
    """
    Interpret a three-point chevron spanning a cell
    border as an inequality sign.

    The vertex points toward the smaller digit.
    Returns (lesser_cell, greater_cell) or None.
    """
    if len(waypoints) != 3:
        return None

    (r0, c0), (r1, c1), (r2, c2) = waypoints

    # Wings share a row: the chevron crosses a
    # horizontal border (vertical cell pair).
    if _near(r0, r2) and not _near(c0, c2):
        border = round((r0 + r1) / 2)
        column = (c0 + c2) / 2

        if not _is_half(column):
            return None

        column = int(column)

        if not (
            1 <= border <= size - 1 and 0 <= column < size
        ):
            return None

        upper = (border - 1, column)
        lower = (border, column)

        if r1 < border:
            return upper, lower

        return lower, upper

    # Wings share a column: vertical sign between a
    # horizontal cell pair.
    if _near(c0, c2) and not _near(r0, r2):
        border = round((c0 + c1) / 2)
        row = (r0 + r2) / 2

        if not _is_half(row):
            return None

        row = int(row)

        if not (
            1 <= border <= size - 1 and 0 <= row < size
        ):
            return None

        left = (row, border - 1)
        right = (row, border)

        if c1 < border:
            return left, right

        return right, left

    return None


# ----------------------------------------------------------
# SCL extraction
# ----------------------------------------------------------

def _new_model(source_url, payload, fmt):
    return {
        "format": fmt,
        "title": "",
        "author": "",
        "rules": "",
        "solution": None,
        "source_url": source_url,
        "size": None,
        "givens": {},
        "constraints": {},
        "unrecognized": [],
        "ambiguous": [],
        "manual": [],
        "metadata_strings": [],
        "_border_glyphs": [],
        "raw": payload,
    }


def _set_solution(model, text, origin="metadata"):
    """Validate and store an 81-digit solution string."""
    text = (text or "").strip()

    if len(text) == 81 and all(
        ch in "123456789" for ch in text
    ):
        model["solution"] = text
        return

    model["unrecognized"].append(
        f"Invalid solution string from {origin} "
        f"({len(text)} characters)"
    )


def _add_constraint(model, kind, item):
    bucket = model["constraints"].setdefault(kind, [])

    if item in bucket:
        model["ambiguous"].append(
            f"Duplicate {kind} clue ignored: {item}"
        )
        return

    bucket.append(item)


def _standard_regions(regions, size=SUPPORTED_SIZE):
    expected = []

    for box_r in range(0, size, 3):
        for box_c in range(0, size, 3):
            expected.append(sorted(
                (r, c)
                for r in range(box_r, box_r + 3)
                for c in range(box_c, box_c + 3)
            ))

    actual = sorted(
        sorted((int(r), int(c)) for r, c in region)
        for region in regions
    )

    return actual == sorted(expected)


def parse_scl(data, source_url="", payload=""):
    """Translate a decoded SCL dict into an import model."""
    model = _new_model(source_url, payload, "scl")

    metadata = data.get("metadata") or {}

    model["title"] = (
        metadata.get("title") or metadata.get("t") or ""
    )
    model["author"] = metadata.get("author") or ""
    model["rules"] = metadata.get("rules") or ""

    solution = metadata.get("solution")

    if solution is not None:
        _set_solution(model, solution, "metadata")

    cells = data.get("cells") or data.get("ce") or []

    rows = len(cells)
    cols = max((len(row) for row in cells), default=0)

    if (rows, cols) != (SUPPORTED_SIZE, SUPPORTED_SIZE):
        raise SudokuPadImportError(
            f"Unsupported grid size {rows}x{cols}; only "
            f"9x9 puzzles can be imported"
        )

    model["size"] = (rows, cols)

    for r, row in enumerate(cells):
        for c, cell in enumerate(row):
            if cell is None or cell == "":
                continue

            value = cell

            if isinstance(cell, dict):
                value = cell.get("value", cell.get("v"))

                unknown_keys = set(cell) - {"value", "v"}

                if unknown_keys:
                    model["unrecognized"].append(
                        f"Cell ({r}, {c}) has unsupported "
                        f"attributes: {sorted(unknown_keys)}"
                    )

            if value in (None, ""):
                continue

            try:
                digit = int(value)
            except (TypeError, ValueError):
                model["unrecognized"].append(
                    f"Cell ({r}, {c}) has non-digit "
                    f"content: {value!r}"
                )
                continue

            if not 1 <= digit <= 9:
                model["unrecognized"].append(
                    f"Cell ({r}, {c}) has out-of-range "
                    f"given: {digit}"
                )
                continue

            model["givens"][(r, c)] = digit

    regions = data.get("regions") or data.get("re")

    if regions and not _standard_regions(regions):
        model["unrecognized"].append(
            "Non-standard regions (irregular boxes are "
            "not supported)"
        )

    for overlay in data.get("overlays") or data.get("o") or []:
        _classify_overlay(model, overlay)

    for underlay in (
        data.get("underlays") or data.get("u") or []
    ):
        _classify_underlay(model, underlay)

    for line in data.get("lines") or data.get("l") or []:
        _classify_line(model, line)

    for cage in data.get("cages") or data.get("ca") or []:
        _classify_cage(model, cage)

    for arrow in data.get("arrows") or data.get("a") or []:
        model["unrecognized"].append(
            f"Arrow entity requires manual translation: "
            f"{arrow}"
        )

    _resolve_border_glyphs(model)

    _apply_rule_text(model)

    return model


_BORDER_GLYPHS = ("X", "V", "<", ">", "^", "∧", "∨")


def _classify_overlay(model, overlay):
    if not isinstance(overlay, dict):
        model["unrecognized"].append(
            f"Unparseable overlay: {overlay!r}"
        )
        return

    center = overlay.get("center") or overlay.get("ct")
    width = overlay.get("width", overlay.get("w", 0)) or 0
    rounded = _truthy_flag(
        overlay.get("rounded", overlay.get("r"))
    )
    text = overlay.get("text", overlay.get("te"))
    background = overlay.get(
        "backgroundColor", overlay.get("c2")
    )

    if text is not None:
        glyph = str(text).strip().upper()
        pair = border_pair(center) if center else None

        if pair and glyph in _BORDER_GLYPHS:
            # Meaning depends on the rules text (XV
            # marker versus inequality sign); resolved
            # once all metadata has been read.
            model["_border_glyphs"].append(
                (pair, glyph, tuple(center))
            )
            return

        model["unrecognized"].append(
            f"Text overlay {text!r} at {center}"
        )
        return

    # Small circles on borders are Kropki dot candidates.
    if (
        center
        and rounded
        and width
        and width <= 0.5
        and border_pair(center)
    ):
        pair = border_pair(center)

        if _is_white(background):
            _add_constraint(
                model, "kropki",
                (pair[0], pair[1], "white"),
            )
            return

        if _is_black(background):
            _add_constraint(
                model, "kropki",
                (pair[0], pair[1], "black"),
            )
            return

        model["ambiguous"].append(
            f"Border dot at {center} with color "
            f"{background!r} is neither white nor black"
        )
        return

    model["unrecognized"].append(
        f"Overlay at {center} (width {width}) was not "
        f"recognized"
    )


def _glyph_inequality(pair, glyph):
    """
    Interpret a border glyph as an inequality sign.

    The glyph's point faces the smaller digit, so 'V'
    on a vertical pair means the lower cell is smaller.
    Returns (lesser, greater) or None when the glyph
    does not fit the pair's orientation.
    """
    cell_a, cell_b = pair

    vertical_pair = cell_a[1] == cell_b[1]

    if vertical_pair:
        upper, lower = cell_a, cell_b

        if glyph in ("V", "∨"):
            return lower, upper

        if glyph in ("^", "∧"):
            return upper, lower

    else:
        left, right = cell_a, cell_b

        if glyph == "<":
            return left, right

        if glyph == ">":
            return right, left

    return None


def _resolve_border_glyphs(model):
    """
    Classify collected border glyphs using the rules
    text, after all metadata sources have been read.
    """
    glyphs = model.pop("_border_glyphs", [])

    if not glyphs:
        return

    rules = model["rules"].lower()

    xv_context = any(
        phrase in rules
        for phrase in (
            "sum to 5", "sum to 10", "x or v", "xv",
        )
    )

    inequality_context = (
        "inequalit" in rules
        or "smaller digit" in rules
        or "towards the smaller" in rules
    )

    for pair, glyph, center in glyphs:
        if (
            glyph in ("X", "V")
            and xv_context
            and not inequality_context
        ):
            _add_constraint(
                model, "xv", (pair[0], pair[1], glyph)
            )
            continue

        if inequality_context and not (
            xv_context and glyph in ("X", "V")
        ):
            direction = _glyph_inequality(pair, glyph)

            if direction:
                _add_constraint(
                    model, "inequality", direction
                )
                continue

        model["ambiguous"].append(
            f"Border symbol {glyph!r} at {center} could "
            f"not be confidently classified from the "
            f"rules text"
        )


def _classify_underlay(model, underlay):
    if not isinstance(underlay, dict):
        model["unrecognized"].append(
            f"Unparseable underlay: {underlay!r}"
        )
        return

    if underlay.get("class") == "board-position":
        return  # Pure decoration.

    background = normalize_color(
        underlay.get(
            "backgroundColor", underlay.get("c2", "")
        )
        or ""
    )

    # Fully transparent underlays are decorative.
    if len(background) == 9 and background.endswith("00"):
        return

    model["unrecognized"].append(
        f"Underlay was not recognized: {underlay}"
    )


def _classify_line(model, line):
    if not isinstance(line, dict):
        model["unrecognized"].append(
            f"Unparseable line: {line!r}"
        )
        return

    waypoints = (
        line.get("wayPoints") or line.get("wp") or []
    )

    points = [
        (float(p[0]), float(p[1])) for p in waypoints
    ]

    inequality = chevron_inequality(points)

    if inequality:
        _add_constraint(model, "inequality", inequality)
        return

    # Full-grid diagonals.
    if len(points) == 2:
        (r0, c0), (r1, c1) = points

        if (
            _near(r0, 0) and _near(c0, 0)
            and _near(r1, 9) and _near(c1, 9)
        ) or (
            _near(r0, 9) and _near(c0, 9)
            and _near(r1, 0) and _near(c1, 0)
        ):
            _add_constraint(model, "diagonal", "main")
            return

        if (
            _near(r0, 0) and _near(c0, 9)
            and _near(r1, 9) and _near(c1, 0)
        ) or (
            _near(r0, 9) and _near(c0, 0)
            and _near(r1, 0) and _near(c1, 9)
        ):
            _add_constraint(model, "diagonal", "anti")
            return

    model["ambiguous"].append(
        f"Line with waypoints {waypoints} could not be "
        f"classified; line styles alone do not identify "
        f"a constraint"
    )


_METADATA_PREFIXES = (
    "title", "author", "rules", "solution"
)


def _coerce_cage_sum(value):
    """
    Validate a cage sum: integers, integral floats,
    and numeric strings are accepted. Returns None
    for anything else.
    """
    if isinstance(value, bool):
        return None

    if isinstance(value, int):
        return value

    if isinstance(value, float):
        return int(value) if value.is_integer() else None

    if isinstance(value, str):
        text = value.strip()

        if text.lstrip("-").isdigit():
            return int(text)

    return None


def _classify_cage(model, cage):
    if not isinstance(cage, dict):
        model["unrecognized"].append(
            f"Unparseable cage: {cage!r}"
        )
        return

    cells = cage.get("cells", cage.get("ce"))
    value = cage.get("value", cage.get("v"))

    # Cage-like objects carrying only a prefixed string
    # are SudokuPad metadata, not Killer cages.
    if cells is None and isinstance(value, str):
        prefix, separator, rest = value.partition(":")
        prefix = prefix.strip().lower()

        if separator and prefix in _METADATA_PREFIXES:
            model["metadata_strings"].append(value)

            rest = rest.strip()

            if prefix == "solution":
                _set_solution(
                    model, rest, "cage metadata"
                )
            elif not model[prefix]:
                model[prefix] = rest

            return

        model["unrecognized"].append(
            f"Cage-like object with unknown metadata "
            f"prefix: {value!r}"
        )
        return

    if not cells:
        model["unrecognized"].append(
            f"Cage without cells: {cage}"
        )
        return

    total = _coerce_cage_sum(value)

    if total is None:
        model["unrecognized"].append(
            f"Cage without a valid integer sum: {cage}"
        )
        return

    converted = []

    for cell in cells:
        try:
            r, c = int(cell[0]), int(cell[1])
        except (TypeError, ValueError, IndexError):
            model["unrecognized"].append(
                f"Cage with invalid cell {cell!r}: {cage}"
            )
            return

        if not (
            0 <= r < SUPPORTED_SIZE
            and 0 <= c < SUPPORTED_SIZE
        ):
            model["unrecognized"].append(
                f"Cage cell out of bounds {cell!r}: {cage}"
            )
            return

        converted.append((r, c))

    _add_constraint(
        model, "killer",
        (tuple(converted), total),
    )


# ----------------------------------------------------------
# fpuzzles extraction (subset)
# ----------------------------------------------------------

_FPUZ_CELL = re.compile(r"R(\d+)C(\d+)")


def fpuz_cell(text):
    """Convert an fpuzzles R1C1 string to (row, col)."""
    match = _FPUZ_CELL.fullmatch(text.strip())

    if not match:
        raise SudokuPadImportError(
            f"Invalid fpuzzles cell: {text!r}"
        )

    return int(match.group(1)) - 1, int(match.group(2)) - 1


def parse_fpuzzles(data, source_url="", payload=""):
    """Translate an fpuzzles dict into an import model."""
    model = _new_model(source_url, payload, "fpuzzles")

    model["title"] = data.get("title") or ""
    model["author"] = data.get("author") or ""
    model["rules"] = data.get("ruleset") or ""

    size = data.get("size", 9)

    if size != SUPPORTED_SIZE:
        raise SudokuPadImportError(
            f"Unsupported grid size {size}x{size}; only "
            f"9x9 puzzles can be imported"
        )

    model["size"] = (size, size)

    for r, row in enumerate(data.get("grid") or []):
        for c, cell in enumerate(row):
            if not isinstance(cell, dict):
                continue

            value = cell.get("value")

            if value and cell.get("given", True):
                model["givens"][(r, c)] = int(value)

    simple_lists = {
        "difference": ("kropki", "white"),
        "ratio": ("kropki", "black"),
    }

    for key, (kind, dot_type) in simple_lists.items():
        for entry in data.get(key) or []:
            cells = [
                fpuz_cell(cell)
                for cell in entry.get("cells", [])
            ]

            custom = entry.get("value")

            if custom not in (None, "", "1", "2", 1, 2):
                model["unrecognized"].append(
                    f"{key} clue with custom value "
                    f"{custom!r}"
                )
                continue

            if len(cells) == 2:
                _add_constraint(
                    model, kind,
                    (cells[0], cells[1], dot_type),
                )

    for entry in data.get("xv") or []:
        cells = [
            fpuz_cell(cell)
            for cell in entry.get("cells", [])
        ]
        marker = (entry.get("value") or "").upper()

        if len(cells) == 2 and marker in ("X", "V"):
            _add_constraint(
                model, "xv", (cells[0], cells[1], marker)
            )
        else:
            model["unrecognized"].append(
                f"XV clue not understood: {entry}"
            )

    for key, kind in (
        ("thermometer", "thermometer"),
        ("palindrome", "palindrome"),
        ("renban", "renban"),
        ("whispers", "whispers"),
        ("betweenline", "between"),
    ):
        for entry in data.get(key) or []:
            for line in entry.get("lines", []):
                _add_constraint(
                    model, kind,
                    tuple(fpuz_cell(cell) for cell in line),
                )

    for entry in data.get("arrow") or []:
        circle = [
            fpuz_cell(cell)
            for cell in entry.get("cells", [])
        ]

        for line in entry.get("lines", []):
            shaft = [fpuz_cell(cell) for cell in line]

            # fpuzzles arrow lines start on the circle.
            shaft = [
                cell for cell in shaft
                if cell not in circle
            ]

            if circle and shaft:
                _add_constraint(
                    model, "arrow",
                    (tuple(circle), tuple(shaft)),
                )

    for entry in data.get("killercage") or []:
        cells = tuple(
            fpuz_cell(cell)
            for cell in entry.get("cells", [])
        )

        try:
            total = int(entry.get("value"))
        except (TypeError, ValueError):
            model["unrecognized"].append(
                f"Killer cage without numeric sum: {entry}"
            )
            continue

        _add_constraint(model, "killer", (cells, total))

    for entry in data.get("odd") or []:
        _add_constraint(
            model, "parity",
            (fpuz_cell(entry["cell"]), "odd"),
        )

    for entry in data.get("even") or []:
        _add_constraint(
            model, "parity",
            (fpuz_cell(entry["cell"]), "even"),
        )

    if data.get("diagonal+"):
        _add_constraint(model, "diagonal", "anti")

    if data.get("diagonal-"):
        _add_constraint(model, "diagonal", "main")

    if data.get("antiknight"):
        _add_constraint(model, "global", "anti-knight")

    if data.get("antiking"):
        _add_constraint(model, "global", "anti-king")

    if data.get("nonconsecutive"):
        _add_constraint(model, "global", "nonconsecutive")

    if data.get("negative"):
        model["manual"].append(
            f"fpuzzles negative toggles need manual "
            f"review: {data['negative']}"
        )

    known_keys = {
        "title", "author", "ruleset", "size", "grid",
        "difference", "ratio", "xv", "thermometer",
        "palindrome", "renban", "whispers", "betweenline",
        "arrow", "killercage", "odd", "even",
        "diagonal+", "diagonal-", "antiknight", "antiking",
        "nonconsecutive", "negative", "solution",
        "highlightConflicts", "text", "line", "circle",
        "rectangle",
    }

    for key in data:
        if key not in known_keys:
            model["unrecognized"].append(
                f"fpuzzles feature {key!r} is not supported"
            )

    for key in ("text", "line", "circle", "rectangle"):
        if data.get(key):
            model["ambiguous"].append(
                f"Cosmetic fpuzzles {key!r} elements "
                f"need manual review"
            )

    solution = data.get("solution")

    if isinstance(solution, list) and all(
        solution
    ):
        model["solution"] = "".join(
            str(v) for v in solution
        )

    _apply_rule_text(model)

    return model


# ----------------------------------------------------------
# Rules-text cross-checking
# ----------------------------------------------------------

_RULE_EXPECTATIONS = (
    ("kropki", ("white dot", "black dot", "kropki")),
    ("inequality", ("inequality", "greater than")),
    ("xv", (" xv ", "x or v", "sum to 5", "sum to 10")),
    ("thermometer", ("thermometer", "thermo")),
    ("killer", ("cage",)),
    ("arrow", ("arrow",)),
    ("whispers", ("whisper",)),
    ("renban", ("renban",)),
    ("palindrome", ("palindrome",)),
    ("between", ("between line", "between the",)),
    ("little-killer", ("little killer",)),
    ("parity", ("odd digit", "even digit", "odd/even")),
    ("diagonal", ("diagonal",)),
)

_GLOBAL_RULES = (
    ("anti-knight", ("anti-knight", "antiknight",
                     "knight's move", "knights move")),
    ("anti-king", ("anti-king", "antiking",
                   "king's move", "kings move")),
    ("nonconsecutive", ("non-consecutive",
                        "nonconsecutive")),
)


def _apply_rule_text(model):
    rules = f" {model['rules'].lower()} "

    if not rules.strip():
        if model["constraints"]:
            model["manual"].append(
                "No rules text was provided; constraint "
                "interpretation cannot be confirmed"
            )
        return

    # Global rules stated in the text.
    for name, phrases in _GLOBAL_RULES:
        if any(phrase in rules for phrase in phrases):
            bucket = model["constraints"].setdefault(
                "global", []
            )

            if name not in bucket:
                bucket.append(name)

    # Negative Kropki/XV only on explicit statements.
    if (
        "all dots are given" in rules
        and "not all dots" not in rules
    ):
        model["constraints"].setdefault(
            "global", []
        ).append("negative-kropki")
        model["manual"].append(
            "Negative Kropki enabled from rules text "
            "('all dots are given'); verify wording"
        )

    if (
        ("all x" in rules or "all v" in rules)
        and "not all" not in rules
    ):
        model["manual"].append(
            "Rules may imply negative XV; verify wording"
        )

    # Geometry without matching rules text is ambiguous;
    # rules text without matching geometry needs manual
    # interpretation.
    for kind, phrases in _RULE_EXPECTATIONS:
        mentioned = any(
            phrase in rules for phrase in phrases
        )
        present = bool(model["constraints"].get(kind))

        if present and not mentioned:
            model["ambiguous"].append(
                f"{kind} clues were detected visually "
                f"but the rules text does not mention "
                f"them; they may be decorative"
            )

        if mentioned and not present and kind not in (
            "between",
        ):
            model["manual"].append(
                f"Rules mention {kind} but no matching "
                f"clues were translated"
            )


def classify_import(model):
    """Classify the import as a whole."""
    if model["unrecognized"]:
        if (
            len(model["unrecognized"])
            > len(model["constraints"])
        ):
            return "Unsupported"

        return "Needs Review"

    if model["ambiguous"] or model["manual"]:
        return "Needs Review"

    return "Complete"


# ----------------------------------------------------------
# Module generation
# ----------------------------------------------------------

_METHOD_MAP = {
    "kropki": "add_kropki_dot",
    "xv": "add_xv",
    "inequality": "add_inequality",
}


def generate_module(model, module_name):
    """Render the Python puzzle module source."""
    title = (model["title"] or "Untitled").strip()
    author = (model["author"] or "Unknown").strip()

    diagonals = set(
        model["constraints"].get("diagonal", [])
    )

    single_diagonals = (
        sorted(diagonals)
        if diagonals and not {"main", "anti"} <= diagonals
        else []
    )

    lines = []

    rules = model["rules"].replace("\\", "\\\\")

    lines.append('"""')
    lines.append(f"{title} by {author}")
    lines.append("")
    lines.append(
        f"Imported from {model['source_url']}"
        if model["source_url"]
        else "Imported from SudokuPad data"
    )
    lines.append("")
    lines.append("Rules:")

    for rule_line in rules.splitlines():
        lines.append(rule_line)

    lines.append('"""')
    lines.append("")
    lines.append("from sudoku.puzzle import SudokuPuzzle")

    if single_diagonals:
        lines.append(
            "from sudoku.constraints import "
            "AllDifferentConstraint"
        )

    lines.append("")
    lines.append(f'NAME = "{title} — {author}"')

    if model["source_url"]:
        lines.append(
            f'SOURCE_URL = "{model["source_url"]}"'
        )

    if model["solution"]:
        lines.append("")
        lines.append(
            "# Solution string provided by the source "
            "puzzle data."
        )
        lines.append(f'SOLUTION = "{model["solution"]}"')

    lines.append("")
    lines.append("")
    lines.append("def create_puzzle():")
    lines.append("    grid = [")

    for r in range(9):
        row = [
            model["givens"].get((r, c), 0)
            for c in range(9)
        ]
        lines.append(f"        {row},")

    lines.append("    ]")
    lines.append("")
    lines.append("    puzzle = SudokuPuzzle(grid)")

    constraints = model["constraints"]

    for a, b, dot_type in constraints.get("kropki", []):
        lines.append(
            f"    puzzle.add_kropki_dot("
            f"{a}, {b}, \"{dot_type}\")"
        )

    for a, b, marker in constraints.get("xv", []):
        lines.append(
            f"    puzzle.add_xv({a}, {b}, \"{marker}\")"
        )

    for lesser, greater in constraints.get(
        "inequality", []
    ):
        lines.append(
            f"    puzzle.add_inequality("
            f"{lesser}, {greater}, \"<\")"
        )

    for cells in constraints.get("thermometer", []):
        lines.append(
            f"    puzzle.add_thermometer({list(cells)})"
        )

    for cells in constraints.get("whispers", []):
        lines.append(
            f"    puzzle.add_german_whispers({list(cells)})"
        )

    for cells in constraints.get("renban", []):
        lines.append(
            f"    puzzle.add_renban({list(cells)})"
        )

    for cells in constraints.get("palindrome", []):
        lines.append(
            f"    puzzle.add_palindrome({list(cells)})"
        )

    for cells in constraints.get("between", []):
        lines.append(
            f"    puzzle.add_between_line({list(cells)})"
        )

    for circle, shaft in constraints.get("arrow", []):
        lines.append(
            f"    puzzle.add_arrow("
            f"{list(circle)}, {list(shaft)})"
        )

    for cells, total in constraints.get("killer", []):
        lines.append(
            f"    puzzle.add_killer_cage("
            f"{list(cells)}, {total})"
        )

    for cells, total in constraints.get(
        "little-killer", []
    ):
        lines.append(
            f"    puzzle.add_little_killer("
            f"{list(cells)}, {total})"
        )

    for cell, parity in constraints.get("parity", []):
        method = (
            "add_odd_cell" if parity == "odd"
            else "add_even_cell"
        )
        lines.append(f"    puzzle.{method}({cell})")

    diagonals = set(constraints.get("diagonal", []))

    if {"main", "anti"} <= diagonals:
        lines.append(
            "    puzzle.add_diagonal_constraints()"
        )
    else:
        for diagonal in single_diagonals:
            if diagonal == "main":
                cells = [(i, i) for i in range(9)]
                comment = "Main diagonal only."
            else:
                cells = [(i, 8 - i) for i in range(9)]
                comment = "Anti-diagonal only."

            lines.append("")
            lines.append(f"    # {comment}")
            lines.append("    puzzle.add_constraint(")
            lines.append("        AllDifferentConstraint(")
            lines.append(f"            {cells},")
            lines.append(
                "            "
                "required_values=set(range(1, 10)),"
            )
            lines.append("        )")
            lines.append("    )")

    for rule in constraints.get("global", []):
        method = {
            "anti-knight": "add_anti_knight_constraints",
            "anti-king": "add_anti_king_constraints",
            "nonconsecutive":
                "add_nonconsecutive_constraints",
            "negative-kropki":
                "add_negative_kropki_constraints",
        }.get(rule)

        if method:
            lines.append(f"    puzzle.{method}()")

    lines.append("")
    lines.append("    return puzzle")
    lines.append("")

    return "\n".join(lines)


def write_module(model, module_name, force=False):
    """Write the generated module into puzzles/."""
    path = PROJECT_ROOT / "puzzles" / f"{module_name}.py"

    if path.exists() and not force:
        raise SudokuPadImportError(
            f"{path} already exists; pass --force to "
            f"overwrite it"
        )

    path.write_text(
        generate_module(model, module_name),
        encoding="utf-8",
    )

    return path


# ----------------------------------------------------------
# Import report
# ----------------------------------------------------------

def build_report(model):
    """Render a human-readable import report."""
    classification = classify_import(model)

    lines = []
    lines.append("SUDOKUPAD IMPORT REPORT")
    lines.append(f"Title:   {model['title']}")
    lines.append(f"Author:  {model['author']}")
    lines.append(f"Source:  {model['source_url']}")
    lines.append(f"Format:  {model['format']}")
    lines.append(
        f"Grid:    "
        f"{model['size'][0]}x{model['size'][1]}"
    )
    lines.append(f"Givens:  {len(model['givens'])}")
    lines.append(
        f"Solution provided: "
        f"{'yes' if model['solution'] else 'no'}"
    )

    lines.append("")
    lines.append("Imported constraints:")

    if model["constraints"]:
        for kind in sorted(model["constraints"]):
            entries = model["constraints"][kind]
            lines.append(
                f"  {kind}: {len(entries)}"
            )

            for entry in entries:
                lines.append(f"    {entry}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Unrecognized elements:")

    for item in model["unrecognized"] or ["  (none)"]:
        lines.append(
            f"  {item}" if not item.startswith(" ")
            else item
        )

    lines.append("")
    lines.append("Ambiguous visual clues:")

    for item in model["ambiguous"] or ["  (none)"]:
        lines.append(
            f"  {item}" if not item.startswith(" ")
            else item
        )

    lines.append("")
    lines.append("Rules text requiring manual review:")

    for item in model["manual"] or ["  (none)"]:
        lines.append(
            f"  {item}" if not item.startswith(" ")
            else item
        )

    if model["metadata_strings"]:
        lines.append("")
        lines.append("Original metadata strings:")

        for item in model["metadata_strings"]:
            lines.append(f"  {item}")

    lines.append("")
    lines.append("Full rules text:")

    for rule_line in (model["rules"] or "(none)").splitlines():
        lines.append(f"  {rule_line}")

    lines.append("")
    lines.append(f"Classification: {classification}")

    if classification == "Complete":
        lines.append(
            "The import is complete enough to attempt "
            "solving, but verify against the original "
            "before trusting results."
        )
    elif classification == "Needs Review":
        lines.append(
            "Resolve the items above before attempting "
            "to solve this import."
        )
    else:
        lines.append(
            "Too many elements were unrecognized to "
            "produce a usable import."
        )

    return "\n".join(lines)


# ----------------------------------------------------------
# High-level import flow and CLI
# ----------------------------------------------------------

def import_puzzle(reference, source_url=None):
    """Fetch, decode, and translate a puzzle."""
    kind, value = extract_puzzle_reference(reference)

    if kind == "id":
        payload = fetch_payload(value)
        url = source_url or f"https://sudokupad.app/{value}"
    else:
        payload = value
        url = source_url or ""

    fmt, data = decode_payload(payload)

    if fmt == "scl":
        return parse_scl(data, url, payload)

    return parse_fpuzzles(data, url, payload)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Import a SudokuPad puzzle into a Python "
            "puzzle module."
        )
    )

    parser.add_argument(
        "reference",
        help="SudokuPad URL, short puzzle ID, or raw data.",
    )

    parser.add_argument(
        "--module",
        default=None,
        help=(
            "Module name to generate under puzzles/ "
            "(for example ctc_002). Only written when "
            "the import is Complete, unless --force."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Overwrite an existing module and allow "
            "generation of Needs Review imports."
        ),
    )

    args = parser.parse_args(argv)

    model = import_puzzle(args.reference)

    print(build_report(model))

    classification = classify_import(model)

    if args.module:
        if classification == "Complete" or args.force:
            path = write_module(
                model, args.module, force=args.force
            )
            print(f"\nModule written to {path}")
        else:
            print(
                f"\nModule not written: import is "
                f"{classification}. Use --force to "
                f"write it anyway."
            )

    return model


if __name__ == "__main__":
    main()
