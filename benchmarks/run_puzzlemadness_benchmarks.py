"""Benchmark imported PuzzleMadness puzzles using first-solution search."""

import argparse
import csv
import re
from pathlib import Path
import multiprocessing as mp

from benchmarks.benchmark_utils import (
    benchmark_first_solution,
    discover_puzzle_modules,
)

OUTPUT_FILE = Path("output/puzzlemadness_benchmark_results.csv")

INSTRUMENTED_OUTPUT_FILE = Path(
    "output/puzzlemadness_instrumented_results.csv"
)

CONSTRAINT_OUTPUT_FILE = Path(
    "output/puzzlemadness_constraint_results.csv"
)

METRIC_FIELDNAMES = [
    "initial_candidates",
    "initial_remaining_candidates",
    "initial_candidates_eliminated",
    "initial_propagation_seconds",
    "total_propagation_seconds",
    "candidates_eliminated",
    "constraint_evaluations",
    "constraint_reductions",
    "constraint_checks",
    "constraint_contradictions",
    "validation_contradictions",
    "max_search_depth",
    "failed_branches",
]

CONSTRAINT_FIELDNAMES = [
    "module",
    "puzzle",
    "variant",
    "date",
    "constraint_type",
    "evaluations",
    "reductions",
    "candidates_eliminated",
    "seconds",
    "contradictions",
    "validation_contradictions",
]

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

def append_result(path, result, fieldnames=FIELDNAMES):
    """Append one result immediately so progress survives interruptions."""
    path.parent.mkdir(parents=True, exist_ok=True)

    write_header = not path.exists() or path.stat().st_size == 0

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow(result)

def append_constraint_results(path, row, constraint_types):
    """Save one row per constraint type for a puzzle."""
    for constraint_type, stats in constraint_types.items():
        constraint_row = {
            "module": row["module"],
            "puzzle": row["puzzle"],
            "variant": row["variant"],
            "date": row["date"],
            "constraint_type": constraint_type,
            **stats,
        }

        append_result(
            path,
            constraint_row,
            CONSTRAINT_FIELDNAMES,
        )

def benchmark_worker(module_name, connection, instrument=False):
    """Run one puzzle benchmark in a separate process."""
        
    try:
        import importlib

        module = importlib.import_module(module_name)

        result = benchmark_first_solution(
            getattr(module, "NAME", module_name),
            module.create_puzzle,
            instrument=instrument,
        )

        connection.send(("success", result))

    except Exception as exc:
        connection.send((
            "error",
            f"{type(exc).__name__}: {exc}",
        ))

    finally:
        connection.close()


def benchmark_with_timeout(module_name, timeout, instrument=False):
    """Run one puzzle with a hard wall-clock timeout."""
    context = mp.get_context("spawn")
    parent_conn, child_conn = context.Pipe(duplex=False)

    process = context.Process(
        target=benchmark_worker,
        args=(module_name, child_conn, instrument),
    )

    try:
        process.start()
        child_conn.close()

        if parent_conn.poll(timeout):
            try:
                outcome, payload = parent_conn.recv()
            except EOFError:
                return {
                    "status": "ERROR",
                    "validation": "N/A",
                    "error": "Worker exited without returning a result",
                }

            if outcome == "error":
                return {
                    "status": "ERROR",
                    "validation": "N/A",
                    "error": payload,
                }

            return payload

        if process.is_alive():
            process.terminate()
            process.join()

            return {
                "status": "TIMEOUT",
                "validation": "N/A",
                "error": f"Exceeded {timeout} seconds",
            }

        return {
            "status": "ERROR",
            "validation": "N/A",
            "error": f"Worker exited with code {process.exitcode}",
        }

    finally:
        parent_conn.close()

        if process.is_alive():
            process.terminate()

        process.join()
        process.close()

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument("--variant")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--output", type=Path, default=OUTPUT_FILE)
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--instrument", action="store_true")
    
    args = parser.parse_args(argv)

    if args.instrument:
        if args.output == OUTPUT_FILE:
            args.output = INSTRUMENTED_OUTPUT_FILE

        constraint_output = CONSTRAINT_OUTPUT_FILE
    else:
        constraint_output = None
        
    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")
    
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
            writer = csv.DictWriter(
                file,
                fieldnames=(
                    FIELDNAMES + METRIC_FIELDNAMES
                    if args.instrument
                    else FIELDNAMES
                ),
            )
            writer.writeheader()
            writer.writerows(existing_rows)

    if args.instrument and args.retry_failed and constraint_output.exists():
        with constraint_output.open(
            newline="", encoding="utf-8"
        ) as file:
            kept_constraint_rows = [
                row for row in csv.DictReader(file)
                if row.get("module") in completed
            ]

        with constraint_output.open(
            "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=CONSTRAINT_FIELDNAMES,
            )
            writer.writeheader()
            writer.writerows(kept_constraint_rows)
            
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
            result = benchmark_with_timeout(
                key,
                args.timeout,
                instrument=args.instrument,
            )
            
            row.update(result)
            
            if args.instrument:
                print("Instrumented result keys:", sorted(result.keys()))
                print("Candidate eliminations:", result.get("candidates_eliminated"))
            
            if result["status"] == "SOLVED":
                solved += 1

                print(
                    f"  SOLVED | "
                    f"{result['elapsed_seconds']:.4f}s | "
                    f"{result['search_decisions']} decisions | "
                    f"{result['backtracks']} backtracks"
                )

            elif result["status"] == "TIMEOUT":
                failed += 1
                print(f"  TIMEOUT | Exceeded {args.timeout}s")

            else:
                failed += 1
                print(
                    f"  {result['status']} | "
                    f"{result.get('error', 'No solution found')}"
                )

        except Exception as exc:
            failed += 1

            row.update({
                "status": "ERROR",
                "validation": "N/A",
                "error": f"{type(exc).__name__}: {exc}",
            })

            print(f"  ERROR: {row['error']}")


        if args.instrument:
            constraint_types = row.pop("constraint_types", {})

            append_result(
                args.output,
                row,
                FIELDNAMES + METRIC_FIELDNAMES,
            )

            if constraint_types:
                append_constraint_results(
                    constraint_output,
                    row,
                    constraint_types,
                )

        else:
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