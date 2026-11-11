"""Benchmark imported PuzzleMadness puzzles using first-solution search."""

import argparse
import csv
import re
from pathlib import Path

from benchmarks.benchmark_utils import (
    benchmark_first_solution,
    discover_puzzle_modules,
)

OUTPUT_FILE = Path("output/puzzlemadness_benchmark_results.csv")

FIELDNAMES = [
    "module",
    "puzzle",
    "variant",
    "date",
    "status",
    "validation",
    "givens",
    "constraints",
    "elapsed_seconds",
    "search_decisions",
    "backtracks",
    "propagation_rounds",
    "solving_method",
    "error",
]


def discover_imported_puzzles(year):
    """Find imported PuzzleMadness modules for the requested year."""
    pattern = re.compile(rf"_(?P<year>{year})_(\d{{2}})_(\d{{2}})$")

    modules = {}

    for key, module in discover_puzzle_modules().items():
        if not key.startswith("puzzles.generic."):
            continue

        basename = key.rsplit(".", 1)[-1]

        if not pattern.search(basename):
            continue

        source_url = getattr(module, "SOURCE_URL", "")

        if "puzzlemadness.co.uk" not in source_url:
            continue

        modules[key] = module

    return modules


def load_completed(path):
    """Read previously recorded puzzle results."""
    if not path.exists():
        return set()

    with path.open(newline="", encoding="utf-8") as file:
        return {
            row["module"]
            for row in csv.DictReader(file)
            if row.get("module")
        }


def append_result(path, result):
    """Append one result immediately so progress survives interruptions."""
    path.parent.mkdir(parents=True, exist_ok=True)

    write_header = not path.exists() or path.stat().st_size == 0

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if write_header:
            writer.writeheader()

        writer.writerow(result)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument("--variant")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--output", type=Path, default=OUTPUT_FILE)
    parser.add_argument("--retry-failed", action="store_true")

    args = parser.parse_args(argv)

    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")

    modules = discover_imported_puzzles(args.year)

    if args.variant:
        modules = {
            key: module
            for key, module in modules.items()
            if key.split(".")[2] == args.variant
        }

    completed = load_completed(args.output)

    if args.retry_failed and args.output.exists():
        with args.output.open(newline="", encoding="utf-8") as file:
            completed = {
                row["module"]
                for row in csv.DictReader(file)
                if row.get("status") == "SOLVED"
                and row.get("validation") == "PASS"
            }

        # Rebuild the CSV without previously failed attempts,
        # so retried puzzles do not create duplicate records.
        with args.output.open(newline="", encoding="utf-8") as file:
            existing_rows = [
                row for row in csv.DictReader(file)
                if row.get("module") in completed
            ]

        with args.output.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(existing_rows)

    pending = [
        (key, module)
        for key, module in modules.items()
        if key not in completed
    ]

    if args.limit is not None:
        pending = pending[:args.limit]

    print(f"Discovered: {len(modules)} puzzles")
    print(f"Already completed: {len(modules) - len([k for k in modules if k not in completed])}")
    print(f"Running: {len(pending)} puzzles\n")

    solved = 0
    failed = 0

    for index, (key, module) in enumerate(pending, start=1):
        basename = key.rsplit(".", 1)[-1]
        variant = key.split(".")[2]

        date_match = re.search(r"(\d{4})_(\d{2})_(\d{2})$", basename)

        puzzle_date = (
            "-".join(date_match.groups())
            if date_match else ""
        )

        print(f"[{index}/{len(pending)}] {basename}...", flush=True)

        row = {
            "module": key,
            "puzzle": getattr(module, "NAME", basename),
            "variant": variant,
            "date": puzzle_date,
            "error": "",
        }

        try:
            result = benchmark_first_solution(
                row["puzzle"],
                module.create_puzzle,
            )

            row.update(result)

            if result["status"] == "SOLVED":
                solved += 1
            else:
                failed += 1

            print(
                f"  {result['status']} | "
                f"{result['elapsed_seconds']:.4f}s | "
                f"{result['search_decisions']} decisions | "
                f"{result['backtracks']} backtracks"
            )

        except Exception as exc:
            failed += 1

            row.update({
                "status": "ERROR",
                "validation": "N/A",
                "error": f"{type(exc).__name__}: {exc}",
            })

            print(f"  ERROR: {row['error']}")

        append_result(args.output, row)

    print("\n========================================")
    print("PUZZLEMADNESS BENCHMARK SUMMARY")
    print("========================================")
    print(f"Discovered puzzles: {len(modules)}")
    print(f"Processed this run: {len(pending)}")
    print(f"Solved: {solved}")
    print(f"Failed: {failed}")
    print(f"Results: {args.output}")


if __name__ == "__main__":
    main()