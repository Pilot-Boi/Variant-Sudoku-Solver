"""
CTC catalogue compatibility scanner.

Scans the Cracking the Cryptic catalogue CSV and
classifies Sudoku puzzles by how well their constraint
tags match this project's implemented variants:

- Potentially compatible: every tag is supported.
- Nearly compatible: one or two unsupported tags.
- Unsupported: more than two unsupported tags.

Important: catalogue tags alone do not guarantee
compatibility. Unusual grid sizes, incomplete clues,
ambiguity, and specialized rules are flagged for manual
review, and even "potentially compatible" puzzles must
have their full instructions checked before they can be
considered solvable by this project.

Usage:
    python -m tools.ctc_catalogue_filter
    python -m tools.ctc_catalogue_filter --min-minutes 60 --top 50
    python -m tools.ctc_catalogue_filter --catalogue path/to/other.csv
"""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_CATALOGUE = (
    PROJECT_ROOT
    / "data"
    / "Cracking the Cryptic Catalogue - Catalogue.csv"
)

DEFAULT_CONFIG = Path(__file__).resolve().parent / (
    "supported_constraints.json"
)

OUTPUT_DIR = PROJECT_ROOT / "output"

COMPATIBLE_FILE = "ctc_compatible.csv"
NEARLY_FILE = "ctc_nearly_compatible.csv"
MISSING_FILE = "ctc_missing_constraints.csv"

MAX_CONSTRAINT_COLUMNS = 12

REVIEW_CAVEAT = (
    "Tags alone do not guarantee compatibility; "
    "verify the full puzzle instructions."
)


def load_config(path=DEFAULT_CONFIG):
    """Load the editable supported-constraints config."""
    with Path(path).open(encoding="utf-8") as file:
        raw = json.load(file)

    aliases = {
        key.lower(): value
        for key, value in raw.get("aliases", {}).items()
    }

    return {
        "supported": {
            name.lower(): name
            for name in raw.get("supported", [])
        },
        "aliases": aliases,
        "manual_review": {
            name.lower(): name
            for name in raw.get("manual_review", [])
        },
    }


def normalize_tag(tag, config):
    """
    Map a raw catalogue tag to its canonical name.

    Unknown tags are returned (stripped) rather than
    discarded.
    """
    tag = tag.strip()

    if not tag:
        return None

    return config["aliases"].get(tag.lower(), tag)


def _find_header(reader):
    """
    Skip leading blank rows and return the header row.

    The catalogue starts with one blank row; the real
    headers follow on the next row.
    """
    for row in reader:
        if any(cell.strip() for cell in row):
            if "Supercat" not in row:
                raise ValueError(
                    "Catalogue header row with 'Supercat' "
                    "column not found"
                )

            return row

    raise ValueError("Catalogue file is empty")


def _column_map(header):
    """
    Resolve column indices, tolerating the catalogue's
    duplicate header names (first occurrence wins) and
    its 'Constraint 1', '2', ..., '12' numbering.
    """
    indices = {}

    for position, name in enumerate(header):
        if name and name not in indices:
            indices[name] = position

    constraint_columns = []

    start = indices.get("Constraint 1")

    if start is not None:
        constraint_columns.append(start)

        for offset in range(2, MAX_CONSTRAINT_COLUMNS + 1):
            position = start + offset - 1

            if position >= len(header):
                break

            if header[position] in (
                str(offset), f"Constraint {offset}"
            ):
                constraint_columns.append(position)

    return indices, constraint_columns


def _cell(row, indices, name):
    position = indices.get(name)

    if position is None or position >= len(row):
        return ""

    return row[position].strip()


def _parse_seconds(text):
    try:
        return int(float(text))
    except (TypeError, ValueError):
        return 0


def parse_catalogue(path, config):
    """
    Read the catalogue and return (records, stats).

    records: one record per Sudoku row
    (Supercat == "Sudoku").
    stats: entry counts for the whole input file.
    """
    records = []
    total_entries = 0

    with Path(path).open(
        encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.reader(file)

        header = _find_header(reader)
        indices, constraint_columns = _column_map(header)

        for row in reader:
            if not any(cell.strip() for cell in row):
                continue

            total_entries += 1

            if _cell(row, indices, "Supercat") != "Sudoku":
                continue

            # Union of the semicolon list and the
            # individual constraint columns, so no tag
            # is silently discarded.
            raw_tags = []

            combined = _cell(
                row, indices, "Puzzle Sub-Type / Constraints"
            )

            raw_tags.extend(combined.split(";"))

            for position in constraint_columns:
                if position < len(row):
                    raw_tags.append(row[position])

            tags = []

            for raw in raw_tags:
                tag = normalize_tag(raw, config)

                if tag and tag not in tags:
                    tags.append(tag)

            records.append({
                "video_title": _cell(row, indices, "Video Title"),
                "puzzle_title": _cell(row, indices, "Puzzle Title"),
                "setter": _cell(row, indices, "Setter"),
                "host": _cell(row, indices, "Host/Solver"),
                "link": _cell(row, indices, "Link YT"),
                "length": _cell(row, indices, "Length"),
                "seconds": _parse_seconds(
                    _cell(row, indices, "Time (s)")
                ),
                "tags": tags,
            })

    stats = {
        "total_entries": total_entries,
        "sudoku_entries": len(records),
        "excluded_entries": total_entries - len(records),
    }

    return records, stats


def classify_records(records, config):
    """
    Attach missing-constraint and review-flag data and
    split records into compatibility buckets.
    """
    supported = config["supported"]
    manual_review = config["manual_review"]

    compatible = []
    nearly = []
    unsupported = []

    for record in records:
        missing = [
            tag for tag in record["tags"]
            if tag.lower() not in supported
        ]

        flags = [
            tag for tag in record["tags"]
            if tag.lower() in manual_review
        ]

        if not record["tags"]:
            flags = ["No constraint tags listed"]

        record["missing"] = missing
        record["flags"] = flags

        if not missing:
            compatible.append(record)
        elif len(missing) <= 2:
            nearly.append(record)
        else:
            unsupported.append(record)

    return compatible, nearly, unsupported


def rank_missing_constraints(nearly, unsupported):
    """
    Rank unsupported tags by how many additional puzzles
    implementing them would unlock.

    "Unlocks alone" counts puzzles where the tag is the
    only unsupported one.
    """
    unlocks = Counter()
    nearly_appearances = Counter()
    total = Counter()

    for record in nearly:
        for tag in record["missing"]:
            nearly_appearances[tag] += 1

            if len(record["missing"]) == 1:
                unlocks[tag] += 1

    for record in nearly + unsupported:
        for tag in record["missing"]:
            total[tag] += 1

    ranked = sorted(
        total,
        key=lambda tag: (
            -unlocks[tag],
            -nearly_appearances[tag],
            -total[tag],
            tag.lower(),
        ),
    )

    return [
        {
            "constraint": tag,
            "unlocks_alone": unlocks[tag],
            "nearly_appearances": nearly_appearances[tag],
            "total_appearances": total[tag],
        }
        for tag in ranked
    ]


def sort_by_duration(records):
    return sorted(
        records,
        key=lambda record: record["seconds"],
        reverse=True,
    )


def _puzzle_row(record, include_missing):
    row = {
        "Video Title": record["video_title"],
        "Puzzle Title": record["puzzle_title"],
        "Setter": record["setter"],
        "Host/Solver": record["host"],
        "Link YT": record["link"],
        "Length": record["length"],
        "Time (s)": record["seconds"],
        "Constraints": "; ".join(record["tags"]),
        "Review Flags": "; ".join(record["flags"]),
    }

    if include_missing:
        row["Missing Constraints"] = "; ".join(
            record["missing"]
        )

    return row


def write_outputs(
    compatible, nearly, ranking, output_dir=OUTPUT_DIR
):
    """Write the three result CSV files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    puzzle_fields = [
        "Video Title",
        "Puzzle Title",
        "Setter",
        "Host/Solver",
        "Link YT",
        "Length",
        "Time (s)",
        "Constraints",
        "Review Flags",
    ]

    nearly_fields = puzzle_fields[:-1] + [
        "Missing Constraints",
        "Review Flags",
    ]

    paths = {}

    paths["compatible"] = output_dir / COMPATIBLE_FILE

    with paths["compatible"].open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=puzzle_fields)
        writer.writeheader()
        writer.writerows(
            _puzzle_row(record, include_missing=False)
            for record in compatible
        )

    paths["nearly"] = output_dir / NEARLY_FILE

    with paths["nearly"].open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=nearly_fields)
        writer.writeheader()
        writer.writerows(
            _puzzle_row(record, include_missing=True)
            for record in nearly
        )

    paths["missing"] = output_dir / MISSING_FILE

    with paths["missing"].open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Constraint",
                "Unlocks Alone",
                "Appears In Nearly Compatible",
                "Total Appearances",
            ],
        )

        writer.writeheader()

        writer.writerows(
            {
                "Constraint": entry["constraint"],
                "Unlocks Alone": entry["unlocks_alone"],
                "Appears In Nearly Compatible": (
                    entry["nearly_appearances"]
                ),
                "Total Appearances": entry["total_appearances"],
            }
            for entry in ranking
        )

    return paths


def run(
    catalogue=DEFAULT_CATALOGUE,
    config_path=DEFAULT_CONFIG,
    min_minutes=None,
    top=None,
    output_dir=OUTPUT_DIR,
):
    """
    Scan the catalogue and write the result CSVs.

    Compatibility statistics and the missing-constraint
    ranking always cover the full Sudoku catalogue.
    --min-minutes narrows the exported puzzle lists and
    adds a filtered view; --top caps only the number of
    exported rows.
    """
    config = load_config(config_path)

    records, stats = parse_catalogue(catalogue, config)

    compatible, nearly, unsupported = classify_records(
        records, config
    )

    full = {
        "compatible": compatible,
        "nearly": nearly,
        "unsupported": unsupported,
    }

    # Ranked across every Sudoku puzzle, regardless of
    # the CLI filters.
    ranking = rank_missing_constraints(nearly, unsupported)

    filtered = None
    export_compatible = compatible
    export_nearly = nearly

    if min_minutes is not None:
        threshold = min_minutes * 60

        filtered = {
            name: [
                record for record in bucket
                if record["seconds"] >= threshold
            ]
            for name, bucket in full.items()
        }

        export_compatible = filtered["compatible"]
        export_nearly = filtered["nearly"]

    export_compatible = sort_by_duration(export_compatible)
    export_nearly = sort_by_duration(export_nearly)

    if top is not None:
        export_compatible = export_compatible[:top]
        export_nearly = export_nearly[:top]

    paths = write_outputs(
        export_compatible, export_nearly, ranking, output_dir
    )

    return {
        "stats": stats,
        "full": full,
        "filtered": filtered,
        "exported": {
            "compatible": export_compatible,
            "nearly": export_nearly,
        },
        "ranking": ranking,
        "paths": paths,
        "min_minutes": min_minutes,
        "top": top,
    }


def _print_heading(title):
    print()
    print(title)


def _print_stat(label, value):
    if isinstance(value, int):
        value = f"{value:,}"

    print(f"{label:<34}{value:>10}")


def print_summary(results):
    """Print the sectioned console summary."""
    stats = results["stats"]
    full = results["full"]
    filtered = results["filtered"]
    exported = results["exported"]
    ranking = results["ranking"]
    top = results["top"]
    min_minutes = results["min_minutes"]

    print("CATALOGUE OVERVIEW")
    _print_stat("Total entries:", stats["total_entries"])
    _print_stat(
        "Sudoku puzzles analyzed:", stats["sudoku_entries"]
    )
    _print_stat(
        "Non-Sudoku entries excluded:",
        stats["excluded_entries"],
    )

    _print_heading("COMPATIBILITY — FULL CATALOGUE")
    _print_stat(
        "Potentially compatible:", len(full["compatible"])
    )
    _print_stat("Nearly compatible:", len(full["nearly"]))
    _print_stat("Unsupported:", len(full["unsupported"]))

    if filtered is not None:
        _print_heading(
            f"FILTERED RESULTS "
            f"(videos >= {min_minutes:g} minutes)"
        )

        total_filtered = sum(
            len(bucket) for bucket in filtered.values()
        )

        _print_stat(
            "Sudoku puzzles in filter:", total_filtered
        )
        _print_stat(
            "Potentially compatible:",
            len(filtered["compatible"]),
        )
        _print_stat(
            "Nearly compatible:", len(filtered["nearly"])
        )
        _print_stat(
            "Unsupported:", len(filtered["unsupported"])
        )

    _print_heading("CSV EXPORT SUMMARY")
    _print_stat(
        "Maximum rows per puzzle CSV:",
        top if top is not None else "unlimited",
    )
    _print_stat(
        "Compatible puzzles exported:",
        len(exported["compatible"]),
    )
    _print_stat(
        "Nearly compatible exported:",
        len(exported["nearly"]),
    )
    _print_stat(
        "Missing constraints ranked:", len(ranking)
    )

    _print_heading("MISSING CONSTRAINTS (TOP 10)")
    print(
        "Unlocks alone: puzzles whose only unsupported\n"
        "  constraint type is this one.\n"
        "Nearly compatible: puzzles with one or two\n"
        "  unsupported constraint types containing it.\n"
        "Total appearances: Sudoku puzzles containing\n"
        "  the constraint tag."
    )
    print()

    print(
        f"{'Constraint':<26}"
        f"{'Unlocks':>9}{'Nearly':>9}{'Total':>9}"
    )

    for entry in ranking[:10]:
        print(
            f"{entry['constraint']:<26}"
            f"{entry['unlocks_alone']:>9,}"
            f"{entry['nearly_appearances']:>9,}"
            f"{entry['total_appearances']:>9,}"
        )

    print()

    for path in results["paths"].values():
        print(f"Saved {path}")

    print(f"\nNote: {REVIEW_CAVEAT}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Scan the CTC catalogue for puzzles whose "
            "constraint tags this solver may support. "
            + REVIEW_CAVEAT
        )
    )

    parser.add_argument(
        "--catalogue",
        type=Path,
        default=DEFAULT_CATALOGUE,
        help="Path to the catalogue CSV file.",
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to the supported-constraints JSON file.",
    )

    parser.add_argument(
        "--min-minutes",
        type=float,
        default=None,
        help="Only include videos at least this long.",
    )

    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help=(
            "Limit the exported compatible and nearly-"
            "compatible lists to the N longest videos. "
            "Does not affect the scan statistics."
        ),
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory for the result CSV files.",
    )

    args = parser.parse_args(argv)

    results = run(
        catalogue=args.catalogue,
        config_path=args.config,
        min_minutes=args.min_minutes,
        top=args.top,
        output_dir=args.output_dir,
    )

    print_summary(results)


if __name__ == "__main__":
    main()
