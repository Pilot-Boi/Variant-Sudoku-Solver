"""Import PuzzleMadness Sudoku puzzles into the local puzzle library."""

import argparse
import json
import re
from turtle import delay
import urllib.request
from urllib.parse import urlparse

from pathlib import Path
from collections import defaultdict
from datetime import date
import calendar
import time


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PUZZLE_ROOT = PROJECT_ROOT / "puzzles" / "generic"

BASE_URL = "https://puzzlemadness.co.uk"
_last_request_time = None

SUPPORTED_VARIANTS = {
    "antikingsudoku": {
        "folder": "anti_king",
        "prefix": "anti_king",
        "name": "Anti-King Sudoku",
    },
    "antiknightsudoku": {
        "folder": "anti_knight",
        "prefix": "anti_knight",
        "name": "Anti-Knight Sudoku",
    },
    "arrowsudoku": {
        "folder": "arrow",
        "prefix": "arrow",
        "name": "Arrow Sudoku",
    },
    "betweenlinesudoku": {
        "folder": "between_line",
        "prefix": "between_line",
        "name": "Between Lines Sudoku",
    },
    "xsudoku": {
        "folder": "diagonal",
        "prefix": "diagonal",
        "name": "Diagonal Sudoku",
    },
    "germanwhisperlinesudoku": {
        "folder": "german_whisper",
        "prefix": "german_whisper",
        "name": "German Whispers Sudoku",
    },
    "greaterthansudoku": {
        "folder": "inequality",
        "prefix": "inequality",
        "name": "Inequality Sudoku",
    },
    "killersudoku": {
        "folder": "killer",
        "prefix": "killer",
        "name": "Killer Sudoku",
    },
    "kropkisudoku": {
        "folder": "kropki",
        "prefix": "kropki",
        "name": "Kropki Sudoku",
    },
    "littlekillersudoku": {
        "folder": "little_killer",
        "prefix": "little_killer",
        "name": "Little Killer Sudoku",
    },
    "oddevensudoku": {
        "folder": "odd_even",
        "prefix": "odd_even",
        "name": "Odd/Even Sudoku",
    },
    "palindromelinesudoku": {
        "folder": "palindrome",
        "prefix": "palindrome",
        "name": "Palindrome Sudoku",
    },
    "renbansudoku": {
        "folder": "renban",
        "prefix": "renban",
        "name": "Renban Sudoku",
    },
    "sudoku": {
        "folder": "standard",
        "prefix": "standard",
        "name": "Standard Sudoku",
    },
    "thermosudoku": {
        "folder": "thermo",
        "prefix": "thermo",
        "name": "Thermometer Sudoku",
    },
    "sudokuxv": {
        "folder": "xv",
        "prefix": "xv",
        "name": "X/V Sudoku",
    },
}

EXPECTED_RULESETS = {
    "antikingsudoku": {"AntiKing"},
    "antiknightsudoku": {"AntiKnight"},
    "arrowsudoku": {"Arrow"},
    "betweenlinesudoku": {"BetweenLine"},
    "xsudoku": set(),
    "germanwhisperlinesudoku": {"GermanWhisperLine"},
    "greaterthansudoku": {"GreaterThan"},
    "killersudoku": {"KillerClues"},
    "kropkisudoku": {"Kropki"},
    "littlekillersudoku": {"LittleKiller"},
    "oddevensudoku": {"OddEven"},
    "palindromelinesudoku": {"PalindromeLine"},
    "renbansudoku": {"RenbanLine"},
    "sudoku": set(),
    "thermosudoku": {"Thermo"},
    "sudokuxv": {"XV"},
}


class PuzzleMadnessImportError(Exception):
    """Raised when a puzzle cannot be safely imported."""
    
def fetch_page(url):
    """Download a PuzzleMadness puzzle page."""

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; SudokuResearchImporter/1.0)"
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.read().decode("utf-8")

    except Exception as exc:
        raise PuzzleMadnessImportError(
            f"Could not download puzzle page: {exc}"
        ) from exc
        
def extract_puzzle_data(html):
    """Extract the puzzleData object from page HTML."""

    match = re.search(
        r"\b(?:let|const|var)\s+puzzleData\s*=\s*",
        html,
    )

    if not match:
        raise PuzzleMadnessImportError(
            "Could not find puzzleData in the page."
        )

    decoder = json.JSONDecoder()

    try:
        data, _ = decoder.raw_decode(
            html[match.end():].lstrip()
        )
    except json.JSONDecodeError as exc:
        raise PuzzleMadnessImportError(
            f"Invalid puzzleData JSON: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise PuzzleMadnessImportError(
            "puzzleData must be a JSON object."
        )

    return data

def validate_puzzle_data(data):
    """Validate basic puzzle structure and supported rules."""

    variant = data.get("baseURI")

    if variant not in SUPPORTED_VARIANTS:
        raise PuzzleMadnessImportError(
            f"Unsupported variant: {variant!r}"
        )

    if data.get("gridWidth") != 9 or data.get("gridHeight") != 9:
        raise PuzzleMadnessImportError(
            "Only 9x9 Sudoku puzzles are supported."
        )

    grid = data.get("startingGrid")

    if (
        not isinstance(grid, list)
        or len(grid) != 81
        or any(type(value) is not int or not 0 <= value <= 9
               for value in grid)
    ):
        raise PuzzleMadnessImportError(
            "startingGrid must contain 81 integers from 0 to 9."
        )

    expected_layout = [
        (row // 3) * 3 + (col // 3)
        for row in range(9)
        for col in range(9)
    ]

    if data.get("layout") != expected_layout:
        raise PuzzleMadnessImportError(
            "Nonstandard Sudoku regions are not supported yet."
        )

    extra_regions = data.get("extraRegions", [])

    if variant == "xsudoku":
        if not isinstance(extra_regions, list):
            raise PuzzleMadnessImportError(
                "Expected extraRegions to be a list."
            )

    elif extra_regions:
        raise PuzzleMadnessImportError(
            f"Unexpected extraRegions for {variant}."
        )

    rulesets = data.get("rulesets", [])

    if not isinstance(rulesets, list):
        raise PuzzleMadnessImportError(
            "Expected rulesets to be a list."
        )

    variant = data["baseURI"]
    expected = EXPECTED_RULESETS[variant]

    if variant in {"sudoku", "xsudoku"}:
        if rulesets:
            raise PuzzleMadnessImportError(
                "Standard Sudoku must not have extra rulesets."
            )
    else:
        if len(rulesets) != 1:
            raise PuzzleMadnessImportError(
                f"Expected exactly one ruleset for {variant}."
            )

        rule_type = rulesets[0].get("type")

        if rule_type not in expected:
            raise PuzzleMadnessImportError(
                f"Unexpected ruleset {rule_type!r} "
                f"for {variant}."
            )

    actual_types = [
        rule.get("type")
        for rule in rulesets
        if isinstance(rule, dict)
    ]

    if len(actual_types) != len(rulesets):
        raise PuzzleMadnessImportError(
            "Invalid ruleset entry."
        )

    if set(actual_types) != EXPECTED_RULESETS[variant]:
        raise PuzzleMadnessImportError(
            f"Unexpected rulesets for {variant}: {actual_types}"
        )

    if len(actual_types) != len(set(actual_types)):
        raise PuzzleMadnessImportError(
            "Duplicate ruleset types are not supported."
        )

    return variant

def wait_for_request_slot(delay):
    """Ensure a minimum delay between website requests."""

    global _last_request_time

    now = time.monotonic()

    if _last_request_time is not None:
        elapsed = now - _last_request_time
        remaining = delay - elapsed

        if remaining > 0:
            time.sleep(remaining)

    _last_request_time = time.monotonic()
    
def cell_coordinates(index):
    """Convert a flat cell index to (row, column)."""

    if type(index) is not int or not 0 <= index < 81:
        raise PuzzleMadnessImportError(
            f"Invalid cell index: {index!r}"
        )

    return divmod(index, 9)

def convert_cell_path(indices):
    """Convert a sequence of flat indices into coordinates."""

    if not isinstance(indices, list):
        raise PuzzleMadnessImportError(
            "Expected a list of cell indices."
        )

    return [cell_coordinates(index) for index in indices]

def convert_inequalities(rule_data):
    if not isinstance(rule_data, dict):
        raise PuzzleMadnessImportError(
            "Expected GreaterThan data to be a dictionary."
        )

    horizontal = rule_data.get("horizontal")
    vertical = rule_data.get("vertical")

    if not isinstance(horizontal, list) or len(horizontal) != 72:
        raise PuzzleMadnessImportError(
            "GreaterThan horizontal data must contain 72 entries."
        )

    if not isinstance(vertical, list) or len(vertical) != 72:
        raise PuzzleMadnessImportError(
            "GreaterThan vertical data must contain 72 entries."
        )

    if any(type(value) is not int or value not in (0, 1, 2)
           for value in horizontal + vertical):
        raise PuzzleMadnessImportError(
            "GreaterThan values must be 0, 1, or 2."
        )

    inequalities = []

    # Horizontal: 9 rows, 8 gaps per row.
    for index, value in enumerate(horizontal):
        if value == 0:
            continue

        row, col = divmod(index, 8)

        left = (row, col)
        right = (row, col + 1)

        inequalities.append((left, right, value))

    # Vertical: 8 gaps between rows, 9 columns.
    for index, value in enumerate(vertical):
        if value == 0:
            continue

        row, col = divmod(index, 9)

        top = (row, col)
        bottom = (row + 1, col)

        inequalities.append((top, bottom, value))

    return inequalities

def trace_little_killer_diagonal(start_row, start_col, dr, dc):
    cells = []

    row = start_row
    col = start_col

    while 0 <= row < 9 and 0 <= col < 9:
        cells.append((row, col))

        row += dr
        col += dc

    return cells

def convert_little_killer_clue(diagonal_type, position, edge):
    if type(diagonal_type) is not int or diagonal_type not in (0, 1):
        raise PuzzleMadnessImportError(
            f"Invalid Little Killer diagonal type: {diagonal_type!r}"
        )

    if type(position) is not int or not 1 <= position <= 9:
        raise PuzzleMadnessImportError(
            f"Invalid Little Killer position: {position!r}"
        )

    if type(edge) is not int or edge not in (0, 1, 2, 3):
        raise PuzzleMadnessImportError(
            f"Invalid Little Killer edge: {edge!r}"
        )

    # PuzzleMadness positions clues at cell boundaries.
    # The diagonal type determines which side of
    # the boundary the first cell occupies.
    index = (
        position + 1
        if diagonal_type == 0
        else position - 1
    )

    if edge == 0:  # Top
        start = (0, index)
        direction = (
            (1, 1) if diagonal_type == 0
            else (1, -1)
        )

    elif edge == 1:  # Right
        start = (index, 8)
        direction = (
            (1, -1) if diagonal_type == 0
            else (-1, -1)
        )

    elif edge == 2:  # Bottom
        start = (8, index)
        direction = (
            (-1, 1) if diagonal_type == 0
            else (-1, -1)
        )

    else:  # Left
        start = (index, 0)
        direction = (
            (1, 1) if diagonal_type == 0
            else (-1, 1)
        )

    row, col = start

    if not (0 <= row < 9 and 0 <= col < 9):
        raise PuzzleMadnessImportError(
            f"Little Killer clue starts outside the grid: "
            f"{start}, clue={(diagonal_type, position, edge)}"
        )

    return trace_little_killer_diagonal(
        row, col, *direction
    )
    
def validate_little_killer_sum(cells, target_sum, starting_grid):
    given_sum = sum(
        starting_grid[row * 9 + col]
        for row, col in cells
    )

    empty_cells = sum(
        starting_grid[row * 9 + col] == 0
        for row, col in cells
    )

    minimum = given_sum + empty_cells
    maximum = given_sum + 9 * empty_cells

    if not minimum <= target_sum <= maximum:
        raise PuzzleMadnessImportError(
            f"Little Killer sum {target_sum} is impossible "
            f"for cells {cells}. "
            f"Given sum: {given_sum}, "
            f"empty cells: {empty_cells}."
        )
        
def generate_constraint_code(data):
    """Generate Python code for supported variant constraints."""

    variant = data["baseURI"]

    if variant == "sudoku":
        return []

    if variant == "xsudoku":
        return [
            "    puzzle.add_diagonal_constraints()"
        ]
        
    rulesets = data["rulesets"]
    rule_data = rulesets[0]["data"]

    lines = []

    if variant == "antikingsudoku":
        if rule_data is not True:
            raise PuzzleMadnessImportError(
                "Expected AntiKing rule data to be true."
            )

        lines.append("    puzzle.add_anti_king_constraints()")

    elif variant == "antiknightsudoku":
        if rule_data is not True:
            raise PuzzleMadnessImportError(
                "Expected AntiKnight rule data to be true."
            )

        lines.append("    puzzle.add_anti_knight_constraints()")
    
    elif variant == "arrowsudoku":
            if not isinstance(rule_data, list):
                raise PuzzleMadnessImportError(
                    "Invalid Arrow data."
                )
    
            for indices in rule_data:
                cells = convert_cell_path(indices)
    
                if len(cells) < 2 or len(set(cells)) != len(cells):
                    raise PuzzleMadnessImportError(
                        f"Invalid arrow path: {indices!r}"
                    )
    
                circle = [cells[0]]
                path = cells[1:]
    
                lines.append(
                    f"    puzzle.add_arrow({circle!r}, {path!r})"
                )
    
    elif variant == "betweenlinesudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected BetweenLine data to be a list."
            )

        for line_indices in rule_data:
            if not isinstance(line_indices, list):
                raise PuzzleMadnessImportError(
                    "Each Between Line must be a list of cell indices."
                )

            if len(line_indices) < 3:
                raise PuzzleMadnessImportError(
                    "Between Lines must contain at least "
                    "two endpoints and one interior cell."
                )

            cells = convert_cell_path(line_indices)

            if len(set(cells)) != len(cells):
                raise PuzzleMadnessImportError(
                    "Between Line contains duplicate cells."
                )

            lines.append(
                f"    puzzle.add_between_line({cells!r})"
            )
            
    elif variant == "germanwhisperlinesudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected GermanWhisperLine data to be a list."
            )

        for line_indices in rule_data:
            if not isinstance(line_indices, list):
                raise PuzzleMadnessImportError(
                    "Each German Whispers line must be a list."
                )

            if len(line_indices) < 2:
                raise PuzzleMadnessImportError(
                    "German Whispers lines must contain "
                    "at least two cells."
                )

            cells = convert_cell_path(line_indices)

            if len(set(cells)) != len(cells):
                raise PuzzleMadnessImportError(
                    "German Whispers line contains duplicate cells."
                )

            lines.append(
                f"    puzzle.add_german_whispers({cells!r})"
            )
            
    elif variant == "greaterthansudoku":
        inequalities = convert_inequalities(rule_data)

        for first, second, direction in inequalities:
            # Direction mapping must match PuzzleMadness.
            if direction == 1:
                operator = ">"
            else:
                operator = "<"

            lines.append(
                f"    puzzle.add_inequality("
                f"{first!r}, {second!r}, {operator!r})"
            )
            
    elif variant == "killersudoku":
        if not isinstance(rule_data, dict):
            raise PuzzleMadnessImportError(
                "Invalid KillerClues data."
            )

        layout = rule_data.get("layout")
        sums = rule_data.get("cageSums")

        if (
            not isinstance(layout, list)
            or len(layout) != 81
            or not isinstance(sums, list)
        ):
            raise PuzzleMadnessImportError(
                "Invalid killer cage layout or sums."
            )

        cages = defaultdict(list)

        for index, cage_id in enumerate(layout):
            if type(cage_id) is not int or not 0 <= cage_id < len(sums):
                raise PuzzleMadnessImportError(
                    f"Invalid killer cage ID: {cage_id!r}"
                )

            cages[cage_id].append(cell_coordinates(index))

        # Cage IDs may be sparse. Unused entries in cageSums
        # do not represent actual cages.
        if not cages:
            raise PuzzleMadnessImportError(
                "Killer puzzle contains no cages."
            )

        for cage_id, cells in sorted(cages.items()):
            target = sums[cage_id]

            if type(target) is not int or target <= 0:
                raise PuzzleMadnessImportError(
                    f"Invalid killer cage sum: {target!r}"
                )

            lines.append(
                f"    puzzle.add_killer_cage({cells!r}, {target})"
            )

    elif variant == "kropkisudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected Kropki data to be a list."
            )

        dot_types = {
            0: "black",
            1: "white",
        }

        seen_pairs = set()

        for dot_data in rule_data:
            if not isinstance(dot_data, list) or len(dot_data) != 3:
                raise PuzzleMadnessImportError(
                    "Each Kropki dot must contain "
                    "[cell_a, cell_b, dot_type]."
                )

            index_a, index_b, dot_code = dot_data

            if type(dot_code) is not int or dot_code not in dot_types:
                raise PuzzleMadnessImportError(
                    f"Invalid Kropki dot type: {dot_code!r}"
                )

            cell_a = cell_coordinates(index_a)
            cell_b = cell_coordinates(index_b)

            dr = abs(cell_a[0] - cell_b[0])
            dc = abs(cell_a[1] - cell_b[1])

            if dr + dc != 1:
                raise PuzzleMadnessImportError(
                    "Kropki dots must connect "
                    "orthogonally adjacent cells."
                )

            pair = tuple(sorted((cell_a, cell_b)))

            if pair in seen_pairs:
                raise PuzzleMadnessImportError(
                    f"Duplicate Kropki dot between "
                    f"{cell_a} and {cell_b}."
                )

            seen_pairs.add(pair)

            dot_type = dot_types[dot_code]

            lines.append(
                f"    puzzle.add_kropki_dot("
                f"{cell_a!r}, {cell_b!r}, {dot_type!r})"
            )
    
    elif variant == "littlekillersudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected LittleKiller data to be a list."
            )

        for clue in rule_data:
            if not isinstance(clue, list) or len(clue) != 4:
                raise PuzzleMadnessImportError(
                    "Each Little Killer clue must contain "
                    "[diagonal_type, position, edge, target_sum]."
                )

            diagonal_type, position, edge, target_sum = clue

            if type(target_sum) is not int or target_sum <= 0:
                raise PuzzleMadnessImportError(
                    f"Invalid Little Killer sum: {target_sum!r}"
                )

            cells = convert_little_killer_clue(
                diagonal_type, position, edge
            )
            
            validate_little_killer_sum(
                cells,
                target_sum,
                data["startingGrid"]
            )

            if not len(cells) <= target_sum <= 9 * len(cells):
                raise PuzzleMadnessImportError(
                    f"Impossible Little Killer sum {target_sum} "
                    f"for {len(cells)} cells."
                )

            lines.append(
                f"    puzzle.add_little_killer("
                f"{cells!r}, {target_sum}, "
                f"clue_position={(diagonal_type, position, edge)!r})"
            )
    
    elif variant == "oddevensudoku":
        if not isinstance(rule_data, list) or len(rule_data) != 81:
            raise PuzzleMadnessImportError(
                "OddEven data must contain exactly 81 values."
            )

        if any(
            type(value) is not int or value not in (0, 1)
            for value in rule_data
        ):
            raise PuzzleMadnessImportError(
                "OddEven values must be 0 (odd) or 1 (even)."
            )

        for index, value in enumerate(rule_data):
            cell = cell_coordinates(index)

            if value == 1:
                lines.append(
                    f"    puzzle.add_even_cell({cell!r})"
                )
            else:
                lines.append(
                    f"    puzzle.add_odd_cell({cell!r})"
                )
        
        for index, value in enumerate(rule_data):
            given = data["startingGrid"][index]

            if given != 0 and (given % 2 == 0) != (value == 1):
                raise PuzzleMadnessImportError(
                    f"Parity mismatch at {cell_coordinates(index)}: "
                    f"given {given}, parity code {value}."
                )
    
    elif variant == "palindromelinesudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected PalindromeLine data to be a list."
            )

        for line_indices in rule_data:
            if not isinstance(line_indices, list):
                raise PuzzleMadnessImportError(
                    "Each Palindrome line must be a list."
                )

            if len(line_indices) < 2:
                raise PuzzleMadnessImportError(
                    "Palindrome lines must contain at least two cells."
                )

            cells = convert_cell_path(line_indices)

            if len(set(cells)) != len(cells):
                raise PuzzleMadnessImportError(
                    "Palindrome line contains duplicate cells."
                )

            for a, b in zip(cells, cells[1:]):
                dr = abs(a[0] - b[0])
                dc = abs(a[1] - b[1])

                if max(dr, dc) != 1:
                    raise PuzzleMadnessImportError(
                        "Palindrome line contains "
                        "nonadjacent cells."
                    )

            lines.append(
                f"    puzzle.add_palindrome({cells!r})"
            )
    
    elif variant == "renbansudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected RenbanLine data to be a list."
            )

        for line_indices in rule_data:
            if not isinstance(line_indices, list):
                raise PuzzleMadnessImportError(
                    "Each Renban line must be a list."
                )

            if not 2 <= len(line_indices) <= 9:
                raise PuzzleMadnessImportError(
                    "Renban lines must contain between "
                    "2 and 9 cells."
                )

            cells = convert_cell_path(line_indices)

            if len(set(cells)) != len(cells):
                raise PuzzleMadnessImportError(
                    "Renban line contains duplicate cells."
                )

            for a, b in zip(cells, cells[1:]):
                dr = abs(a[0] - b[0])
                dc = abs(a[1] - b[1])

                if max(dr, dc) != 1:
                    raise PuzzleMadnessImportError(
                        "Renban line contains nonadjacent cells."
                    )

            lines.append(
                f"    puzzle.add_renban({cells!r})"
            )
            
    elif variant == "thermosudoku":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Invalid Thermo data."
            )

        for indices in rule_data:
            cells = convert_cell_path(indices)

            if len(cells) < 2 or len(cells) > 9:
                raise PuzzleMadnessImportError(
                    f"Invalid thermometer length: {indices!r}"
                )

            if len(set(cells)) != len(cells):
                raise PuzzleMadnessImportError(
                    f"Repeated cell in thermometer: {indices!r}"
                )

            lines.append(
                f"    puzzle.add_thermometer({cells!r})"
            )
    
    elif variant == "sudokuxv":
        if not isinstance(rule_data, list):
            raise PuzzleMadnessImportError(
                "Expected XV data to be a list."
            )

        markers = {
            5: "V",
            10: "X",
        }

        seen_pairs = set()

        for marker_data in rule_data:
            if not isinstance(marker_data, list) or len(marker_data) != 3:
                raise PuzzleMadnessImportError(
                    "Each XV marker must contain "
                    "[cell_a, cell_b, target_sum]."
                )

            index_a, index_b, target_sum = marker_data

            if type(target_sum) is not int or target_sum not in markers:
                raise PuzzleMadnessImportError(
                    f"Invalid XV target sum: {target_sum!r}"
                )

            cell_a = cell_coordinates(index_a)
            cell_b = cell_coordinates(index_b)

            # XV markers must connect orthogonally adjacent cells.
            dr = abs(cell_a[0] - cell_b[0])
            dc = abs(cell_a[1] - cell_b[1])

            if dr + dc != 1:
                raise PuzzleMadnessImportError(
                    "XV markers must connect "
                    "orthogonally adjacent cells."
                )

            # Prevent duplicate or conflicting markers.
            pair = tuple(sorted((cell_a, cell_b)))

            if pair in seen_pairs:
                raise PuzzleMadnessImportError(
                    f"Duplicate XV marker between "
                    f"{cell_a} and {cell_b}."
                )

            seen_pairs.add(pair)

            marker = markers[target_sum]

            lines.append(
                f"    puzzle.add_xv("
                f"{cell_a!r}, {cell_b!r}, {marker!r})"
            )

    return lines

def generate_module_source(data, url, difficulty):
    """Generate a complete Python puzzle module."""

    variant = validate_puzzle_data(data)
    config = SUPPORTED_VARIANTS[variant]

    source = data.get("source")

    if not isinstance(source, dict):
        raise PuzzleMadnessImportError(
            "Missing puzzle date information."
        )

    try:
        puzzle_date = date(
            source["year"],
            source["month"],
            source["day"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise PuzzleMadnessImportError(
            "Invalid puzzle date."
        ) from exc

    name = f"{config['name']} — {puzzle_date.isoformat()}"

    flat_grid = data["startingGrid"]
    rows = [
        flat_grid[index:index + 9]
        for index in range(0, 81, 9)
    ]

    grid_lines = "\n".join(
        f"        {row!r},"
        for row in rows
    )

    constraint_lines = generate_constraint_code(data)

    constraints = "\n".join(constraint_lines)

    return f'''"""PuzzleMadness {name}."""

from sudoku.puzzle import SudokuPuzzle


NAME = {name!r}
SOURCE_URL = {url!r}
DIFFICULTY = {difficulty!r}


def create_puzzle():
    grid = [
{grid_lines}
    ]

    puzzle = SudokuPuzzle(grid)

{constraints}

    return puzzle
'''

def get_module_path(variant, puzzle_date):
    """Return the destination path for a PuzzleMadness puzzle."""

    if variant not in SUPPORTED_VARIANTS:
        raise PuzzleMadnessImportError(
            f"Unsupported variant: {variant}"
        )

    config = SUPPORTED_VARIANTS[variant]

    module_name = (
        f"{config['prefix']}_{puzzle_date:%Y_%m_%d}"
    )

    return (
        PUZZLE_ROOT
        / config["folder"]
        / f"{module_name}.py"
    )
    
def write_module(data, url, difficulty, force=False):
    """Write a generated puzzle module to the correct directory."""

    variant = validate_puzzle_data(data)
    config = SUPPORTED_VARIANTS[variant]

    source = data["source"]

    try:
        puzzle_date = date(
            source["year"],
            source["month"],
            source["day"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise PuzzleMadnessImportError(
            "Invalid puzzle date."
        ) from exc

    destination = get_module_path(variant, puzzle_date)

    destination.parent.mkdir(parents=True, exist_ok=True)

    init_file = destination.parent / "__init__.py"
    init_file.touch(exist_ok=True)

    if destination.exists() and not force:
        raise PuzzleMadnessImportError(
            f"Puzzle already exists: {destination}. "
            "Use --force to overwrite."
        )

    code = generate_module_source(data, url, difficulty)

    destination.write_text(code, encoding="utf-8")

    return destination

def generate_month_urls(
    variant,
    difficulty,
    year,
    month,
    start_day=1,
    end_day=None,
):
    """Generate PuzzleMadness URLs for a selected date range."""

    if variant not in SUPPORTED_VARIANTS:
        raise PuzzleMadnessImportError(
            f"Unsupported variant: {variant}"
        )

    if difficulty not in {"easy", "medium", "hard", "tough"}:
        raise PuzzleMadnessImportError(
            f"Unsupported difficulty: {difficulty}"
        )

    try:
        days_in_month = calendar.monthrange(year, month)[1]
    except (ValueError, calendar.IllegalMonthError) as exc:
        raise PuzzleMadnessImportError(
            f"Invalid year/month: {year}-{month}"
        ) from exc

    if end_day is None:
        end_day = days_in_month

    if not (1 <= start_day <= end_day <= days_in_month):
        raise PuzzleMadnessImportError(
            f"Invalid day range: {start_day}-{end_day}. "
            f"Month has {days_in_month} days."
        )

    return [
        (
            f"{BASE_URL}/{variant}/{difficulty}/"
            f"{year}/{month}/{day}"
        )
        for day in range(start_day, end_day + 1)
    ]

def import_puzzle(url, force=False):
    """Download, validate, and import one PuzzleMadness puzzle."""

    parts = urlparse(url).path.strip("/").split("/")

    if len(parts) != 5:
        raise PuzzleMadnessImportError(
            "Expected URL format: "
            "/variant/difficulty/year/month/day"
        )

    variant, difficulty, year, month, day = parts

    if variant not in SUPPORTED_VARIANTS:
        raise PuzzleMadnessImportError(
            f"Unsupported variant: {variant}"
        )

    try:
        requested_date = date(
            int(year),
            int(month),
            int(day),
        )
    except ValueError as exc:
        raise PuzzleMadnessImportError(
            f"Invalid puzzle date in URL: {url}"
        ) from exc

    html = fetch_page(url)
    data = extract_puzzle_data(html)

    if data.get("baseURI") != variant:
        raise PuzzleMadnessImportError(
            "URL variant does not match puzzle data."
        )

    source = data.get("source")

    if not isinstance(source, dict):
        raise PuzzleMadnessImportError(
            "Missing puzzle source information."
        )

    try:
        actual_date = date(
            source["year"],
            source["month"],
            source["day"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise PuzzleMadnessImportError(
            "Invalid source date."
        ) from exc

    if actual_date != requested_date:
        raise PuzzleMadnessImportError(
            f"Date mismatch: requested {requested_date}, "
            f"received {actual_date}"
        )

    return write_module(
        data,
        url,
        difficulty,
        force=force,
    )

def import_month(
    variant,
    difficulty,
    year,
    month,
    force=False,
    delay=1.0,
    start_day=1,
    end_day=None,
    dry_run=False,
):
    """Import PuzzleMadness puzzles for a selected month/day range."""

    urls = generate_month_urls(
        variant,
        difficulty,
        year,
        month,
        start_day=start_day,
        end_day=end_day,
    )

    imported = []
    skipped = []
    failed = []

    print(
        f"\nImporting {variant} ({difficulty}) "
        f"for {year}-{month:02d}"
    )

    if dry_run:
        print("DRY RUN — No files will be written or downloaded.")

    print(f"Total dates: {len(urls)}\n")

    for index, url in enumerate(urls, start=1):
        day = int(url.rstrip("/").split("/")[-1])
        puzzle_date = date(year, month, day)

        destination = get_module_path(
            variant,
            puzzle_date,
        )

        print(
            f"[{index}/{len(urls)}] {puzzle_date}",
            flush=True,
        )

        # Check for existing puzzles before downloading.
        if destination.exists() and not force:
            skipped.append(destination)
            print(f"  SKIPPED: {destination.name}")
            continue

        if dry_run:
            print(f"  WOULD IMPORT: {destination.name}")
            continue

        # Respect the delay across month boundaries.
        wait_for_request_slot(delay)

        try:
            imported_path = import_puzzle(
                url,
                force=force,
            )

            imported.append(imported_path)
            print(f"  OK: {imported_path.name}")

        except PuzzleMadnessImportError as exc:
            failed.append((url, str(exc)))
            print(f"  FAILED: {exc}")

    print("\n" + "=" * 60)
    print("IMPORT SUMMARY")
    print("=" * 60)
    print(f"Imported:     {len(imported)}")
    print(f"Skipped:      {len(skipped)}")
    print(f"Failed:       {len(failed)}")

    if dry_run:
        would_import = (
            len(urls)
            - len(imported)
            - len(skipped)
            - len(failed)
        )
        print(f"Would import: {would_import}")

    print(f"Total dates:  {len(urls)}")

    if failed:
        print("\nFailed puzzles:")
        for url, error in failed:
            print(f"  {url}")
            print(f"    {error}")

    return imported, skipped, failed

def import_year(
    variant,
    difficulty,
    year,
    force=False,
    delay=1.0,
    dry_run=False,
):
    """Import every daily puzzle for a variant across an entire year."""

    imported = []
    skipped = []
    failed = []

    print("\n" + "=" * 60)
    print(f"YEARLY IMPORT: {variant} ({difficulty}) — {year}")
    print("=" * 60)

    for month in range(1, 13):
        month_imported, month_skipped, month_failed = import_month(
            variant=variant,
            difficulty=difficulty,
            year=year,
            month=month,
            force=force,
            delay=delay,
            dry_run=dry_run,
        )

        imported.extend(month_imported)
        skipped.extend(month_skipped)
        failed.extend(month_failed)

    print("\n" + "=" * 60)
    print(f"YEARLY IMPORT SUMMARY — {year}")
    print("=" * 60)
    print(f"Imported: {len(imported)}")
    print(f"Skipped:  {len(skipped)}")
    print(f"Failed:   {len(failed)}")
    total_dates = sum(
        calendar.monthrange(year, month)[1]
        for month in range(1, 13)
    )

    would_import = (
        total_dates
        - len(imported)
        - len(skipped)
        - len(failed)
    )

    if dry_run:
        print(f"Would import: {would_import}")

    print(f"Total dates:  {total_dates}")

    return imported, skipped, failed

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Import PuzzleMadness Sudoku puzzles."
    )

    parser.add_argument(
        "url",
        nargs="?",
        help="Import one puzzle using its URL",
    )

    parser.add_argument(
        "--variant",
        choices=sorted(SUPPORTED_VARIANTS),
        help="Puzzle variant for monthly imports",
    )

    parser.add_argument(
        "--difficulty",
        default="hard",
        choices=["easy", "medium", "hard", "tough"],
        help="Puzzle difficulty (default: hard)",
    )

    parser.add_argument(
        "--year",
        type=int,
        help="Year for monthly imports",
    )

    parser.add_argument(
        "--month",
        type=int,
        help="Month for monthly imports",
    )
    
    parser.add_argument(
        "--yearly",
        action="store_true",
        help="Import every month of the specified year",
    )

    parser.add_argument(
    "--start-day",
    type=int,
    default=1,
    help="First day to import (default: 1)",
    )

    parser.add_argument(
        "--end-day",
        type=int,
        help="Last day to import (default: end of month)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview imports without downloading or writing files",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing puzzle modules",
    )

    args = parser.parse_args(argv)

    if args.delay < 0:
        parser.error("--delay cannot be negative")

    try:
        if args.url:
            if any(
                value is not None
                for value in (args.variant, args.year, args.month)
            ):
                parser.error(
                    "Cannot combine a URL with monthly import options."
                )

            parts = urlparse(args.url).path.strip("/").split("/")

            if len(parts) != 5:
                parser.error("Invalid PuzzleMadness URL.")

            variant, difficulty, year, month, day = parts

            try:
                puzzle_date = date(int(year), int(month), int(day))
                destination = get_module_path(variant, puzzle_date)
            except (ValueError, PuzzleMadnessImportError) as exc:
                parser.error(str(exc))

            if destination.exists() and not args.force:
                print(f"SKIPPED: Already imported: {destination}")

            elif args.dry_run:
                print(f"WOULD IMPORT: {destination}")

            else:
                destination = import_puzzle(
                    args.url,
                    force=args.force,
                )
                print(f"Imported: {destination}")

        else:
            if args.variant is None or args.year is None:
                parser.error(
                    "Provide a URL, or specify --variant and --year."
                )

            if args.yearly:
                if args.month is not None:
                    parser.error(
                        "--yearly cannot be combined with --month."
                    )

                if args.start_day != 1 or args.end_day is not None:
                    parser.error(
                        "--start-day and --end-day are only "
                        "supported for monthly imports."
                    )

                imported, skipped, failed = import_year(
                    variant=args.variant,
                    difficulty=args.difficulty,
                    year=args.year,
                    force=args.force,
                    delay=args.delay,
                    dry_run=args.dry_run,
                )

            else:
                if args.url and args.yearly:
                    parser.error(
                        "--yearly cannot be combined with a puzzle URL."
                    )
                    
                if args.month is None:
                    parser.error(
                        "Specify --month for a monthly import, "
                        "or --yearly for an entire year."
                    )

                imported, skipped, failed = import_month(
                    variant=args.variant,
                    difficulty=args.difficulty,
                    year=args.year,
                    month=args.month,
                    force=args.force,
                    delay=args.delay,
                    start_day=args.start_day,
                    end_day=args.end_day,
                    dry_run=args.dry_run,
                )

            if failed:
                raise SystemExit(1)

    except PuzzleMadnessImportError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()