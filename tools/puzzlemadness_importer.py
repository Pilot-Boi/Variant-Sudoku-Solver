"""Import PuzzleMadness Sudoku puzzles into the local puzzle library."""

import argparse
import json
import re
import urllib.request

from pathlib import Path
from collections import defaultdict
from datetime import date


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PUZZLE_ROOT = PROJECT_ROOT / "puzzles" / "generic"

BASE_URL = "https://puzzlemadness.co.uk"

SUPPORTED_VARIANTS = {
    "antikingsudoku": {
        "folder": "anti_king",
        "prefix": "anti_king",
        "name": "Anti-King Sudoku",
    },
    "killersudoku": {
        "folder": "killer",
        "prefix": "killer",
        "name": "Killer Sudoku",
    },
    "arrowsudoku": {
        "folder": "arrow",
        "prefix": "arrow",
        "name": "Arrow Sudoku",
    },
    "thermosudoku": {
        "folder": "thermo",
        "prefix": "thermo",
        "name": "Thermometer Sudoku",
    },
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

EXPECTED_RULESETS = {
    "antikingsudoku": {"AntiKing"},
    "killersudoku": {"KillerClues"},
    "arrowsudoku": {"Arrow"},
    "thermosudoku": {"Thermo"},
}


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

    if data.get("extraRegions"):
        raise PuzzleMadnessImportError(
            "Extra regions are not supported yet."
        )

    rulesets = data.get("rulesets")

    if not isinstance(rulesets, list):
        raise PuzzleMadnessImportError(
            "Missing or invalid rulesets."
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

def generate_constraint_code(data):
    """Generate Python code for supported variant constraints."""

    variant = data["baseURI"]
    ruleset = data["rulesets"][0]
    rule_data = ruleset["data"]

    lines = []

    if variant == "antikingsudoku":
        if rule_data is not True:
            raise PuzzleMadnessImportError(
                "Expected AntiKing rule data to be true."
            )

        lines.append("    puzzle.add_anti_king_constraints()")

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

        if set(cages) != set(range(len(sums))):
            raise PuzzleMadnessImportError(
                "Killer cage IDs and sums do not match."
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

    module_name = (
        f"{config['prefix']}_{puzzle_date:%Y_%m_%d}"
    )

    directory = PUZZLE_ROOT / config["folder"]
    directory.mkdir(parents=True, exist_ok=True)

    # Make sure the directory is importable.
    init_file = directory / "__init__.py"
    init_file.touch(exist_ok=True)

    destination = directory / f"{module_name}.py"

    if destination.exists() and not force:
        raise PuzzleMadnessImportError(
            f"Puzzle already exists: {destination}. "
            "Use --force to overwrite."
        )

    code = generate_module_source(data, url, difficulty)

    destination.write_text(code, encoding="utf-8")

    return destination

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Import a PuzzleMadness Sudoku puzzle."
    )

    parser.add_argument(
        "url",
        help="PuzzleMadness puzzle URL",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing puzzle module",
    )

    args = parser.parse_args(argv)

    try:
        html = fetch_page(args.url)
        data = extract_puzzle_data(html)

        # Parse difficulty from the URL.
        from urllib.parse import urlparse

        parts = urlparse(args.url).path.strip("/").split("/")

        if len(parts) != 5:
            raise PuzzleMadnessImportError(
                "Expected URL format: /variant/difficulty/year/month/day"
            )

        variant, difficulty, year, month, day = parts

        if variant != data.get("baseURI"):
            raise PuzzleMadnessImportError(
                "URL variant does not match puzzle data."
            )

        source = data.get("source", {})

        if (
            str(source.get("year")) != year
            or str(source.get("month")) != str(int(month))
            or str(source.get("day")) != str(int(day))
        ):
            raise PuzzleMadnessImportError(
                "URL date does not match puzzle data."
            )

        destination = write_module(
            data,
            args.url,
            difficulty,
            force=args.force,
        )

        print(f"Imported: {destination}")
        print(f"Variant: {variant}")
        print(f"Difficulty: {difficulty}")
        print(f"Date: {year}-{int(month):02d}-{int(day):02d}")

    except (PuzzleMadnessImportError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()