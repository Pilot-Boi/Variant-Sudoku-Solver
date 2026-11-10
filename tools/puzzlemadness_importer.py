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

EXPECTED_RULESETS = {
    "antikingsudoku": {"AntiKing"},
    "antiknightsudoku": {"AntiKnight"},
    "killersudoku": {"KillerClues"},
    "arrowsudoku": {"Arrow"},
    "thermosudoku": {"Thermo"},
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

    elif variant == "antiknightsudoku":
        if rule_data is not True:
            raise PuzzleMadnessImportError(
                "Expected AntiKnight rule data to be true."
            )

        lines.append("    puzzle.add_anti_knight_constraints()")
    
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