
"""Unified benchmark for controlled Sudoku experiments.

Run from the project root:
    python -m benchmarks.run_controlled_benchmarks --experiment thermometer --limit 10
    python -m benchmarks.run_controlled_benchmarks --experiment thermometer --full
    python -m benchmarks.run_controlled_benchmarks --experiment givens --full
"""
import os
import argparse
import csv
import json
import statistics
import time
import random
from pathlib import Path
import multiprocessing as mp

from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution

DATASETS = {
    "givens": Path("puzzles/controlled/givens_experiment.json"),
    "thermometer": Path("puzzles/controlled/thermometer_experiment.json"),
    "killer": Path("puzzles/controlled/killer_experiment.json"),
    "kropki": Path("puzzles/controlled/kropki_experiment.json"),
    "xv": Path("puzzles/controlled/xv_experiment.json"),
    "inequality": Path("puzzles/controlled/inequality_experiment.json"),
    "parity": Path("puzzles/controlled/parity_experiment.json"),
    "arrow": Path("puzzles/controlled/arrow_experiment.json"),
    "between_line": Path("puzzles/controlled/between_line_experiment.json"),
    "german_whisper": Path("puzzles/controlled/german_whisper_experiment.json"),
    "palindrome": Path("puzzles/controlled/palindrome_experiment.json"),
    "renban": Path("puzzles/controlled/renban_experiment.json"),
    "little_killer": Path("puzzles/controlled/little_killer_experiment.json"),

}

CLUE_VARIANTS = (
    "killer", "kropki", "xv", "inequality", "parity",
    "arrow", "between_line", "german_whisper",
    "palindrome", "renban", "little_killer",
)
CLUE_COUNTS = (2, 4, 6)

METRIC_FIELDS = [
    "initial_candidates",
    "initial_remaining_candidates",
    "initial_candidates_eliminated",
    "candidates_eliminated",
    "constraint_evaluations",
    "constraint_reductions",
    "constraint_checks",
    "constraint_contradictions",
    "validation_contradictions",
    "max_search_depth",
    "failed_branches",
    "total_propagation_seconds",
    "initial_propagation_seconds",
]

FIELDS = [
    "experiment", "id", "base_id", "group",
    "grid_index", "pattern_index", "given_count",
    "condition", "extra_constraint_count", "constraint_count",
    "status", "validation", "reference_match",
    "uniqueness", "uniqueness_seconds",
    "uniqueness_search_decisions",
    "elapsed_seconds", "min_seconds", "max_seconds",
    "timing_trials",
    "search_decisions", "backtracks", "propagation_rounds",
    *METRIC_FIELDS,
    "error",
]


def apply_rules(puzzle, rules):
    if not rules.get("standard", True):
        raise ValueError("Standard Sudoku rules are required")

    for name in ("diagonal", "anti_knight", "anti_king"):
        if rules.get(name, False):
            getattr(puzzle, f"add_{name}_constraints")()


def add_thermometer(puzzle, clue):
    puzzle.add_thermometer([tuple(cell) for cell in clue])


def add_killer_cage(puzzle, clue):
    puzzle.add_killer_cage(
        [tuple(cell) for cell in clue["cells"]],
        clue["sum"],
    )


def add_kropki(puzzle, clue):
    a, b = map(tuple, clue["cells"])
    puzzle.add_kropki_dot(a, b, clue["type"])


def add_xv(puzzle, clue):
    a, b = map(tuple, clue["cells"])
    puzzle.add_xv(a, b, clue["marker"])


def add_inequality(puzzle, clue):
    a, b = map(tuple, clue["cells"])
    puzzle.add_inequality(a, b, clue["operator"])


def add_parity(puzzle, clue):
    cell = tuple(clue["cell"])

    if clue["parity"] == "odd":
        puzzle.add_odd_cell(cell)
    elif clue["parity"] == "even":
        puzzle.add_even_cell(cell)
    else:
        raise ValueError(f"Unknown parity: {clue['parity']}")


def add_arrow(puzzle, clue):
    puzzle.add_arrow(
        [tuple(cell) for cell in clue["circle_cells"]],
        [tuple(cell) for cell in clue["arrow_cells"]],
    )


def add_between_line(puzzle, clue):
    puzzle.add_between_line(
        [tuple(cell) for cell in clue["cells"]]
    )


def add_german_whisper(puzzle, clue):
    puzzle.add_german_whispers(
        [tuple(cell) for cell in clue["cells"]]
    )


def add_palindrome(puzzle, clue):
    puzzle.add_palindrome(
        [tuple(cell) for cell in clue["cells"]]
    )


def add_renban(puzzle, clue):
    puzzle.add_renban(
        [tuple(cell) for cell in clue["cells"]]
    )


def add_little_killer(puzzle, clue):
    puzzle.add_little_killer(
        [tuple(cell) for cell in clue["cells"]],
        clue["sum"],
    )

CONSTRAINT_BUILDERS = {
    "thermometer": add_thermometer,
    "killer": add_killer_cage,
    "kropki": add_kropki,
    "xv": add_xv,
    "inequality": add_inequality,
    "parity": add_parity,
    "arrow": add_arrow,
    "between_line": add_between_line,
    "german_whisper": add_german_whisper,
    "palindrome": add_palindrome,
    "renban": add_renban,
    "little_killer": add_little_killer,
}

def build_puzzle(case, condition):
    puzzle = SudokuPuzzle(case["puzzle"])

    # Baseline: standard Sudoku only.
    if condition == "standard":
        return puzzle

    # Existing controlled variants.
    if condition in ("diagonal", "anti_knight", "anti_king"):
        rules = case["reference_rules"]

        if not rules.get(condition, False):
            raise ValueError(
                f"Condition {condition} is not valid for {case['id']}"
            )

        apply_rules(puzzle, {"standard": True, condition: True})
        return puzzle

    # Thermometer experiments.
    if condition.startswith("thermometer_"):
        count = int(condition.split("_")[-1])

        apply_rules(
            puzzle,
            case.get("solve_rules", {"standard": True}),
        )

        if len(case["thermometers"]) < count:
            raise ValueError("Insufficient thermometer clues")

        for clue in case["thermometers"][:count]:
            CONSTRAINT_BUILDERS["thermometer"](puzzle, clue)

        return puzzle

    # Controlled clue experiments.
    for variant in CLUE_VARIANTS:
        prefix = f"{variant}_"

        if not condition.startswith(prefix):
            continue

        count = int(condition[len(prefix):])

        if count not in CLUE_COUNTS:
            raise ValueError(f"Unsupported clue count: {count}")

        if case["variant"] != variant:
            raise ValueError(
                f"Condition {condition} does not match "
                f"case variant {case['variant']}"
            )

        if len(case["clues"]) < count:
            raise ValueError("Insufficient variant clues")

        apply_rules(
            puzzle,
            case.get("solve_rules", {"standard": True}),
        )

        for clue in case["clues"][:count]:
            CONSTRAINT_BUILDERS[variant](puzzle, clue)

        return puzzle

    raise ValueError(f"Unknown condition: {condition}")

def get_conditions(experiment, case):

    if experiment in CLUE_VARIANTS:
        if case["variant"] != experiment:
            raise ValueError("Dataset variant mismatch")

        return [
            ("standard", 0),
            *[
                (f"{experiment}_{count}", count)
                for count in CLUE_COUNTS
            ],
        ]

    if experiment == "thermometer":
        return [
            ("standard", 0),
            ("thermometer_2", 2),
            ("thermometer_4", 4),
            ("thermometer_6", 6),
        ]

    if experiment == "givens":
        rules = case["reference_rules"]
        enabled = [
            name for name in ("diagonal", "anti_knight", "anti_king")
            if rules.get(name, False)
        ]
        if len(enabled) > 1:
            raise ValueError("Expected at most one extra variant")
        if not enabled:
            return [("standard", 0)]
        return [("standard", 0), (enabled[0], 1)]

    raise ValueError(f"Unknown experiment: {experiment}")


def prepare_cases(experiment, records):

    if experiment in CLUE_VARIANTS:
        # Each generated dataset contains records for 2, 4,
        # and 6 clues. Keep only the six-clue record,
        # then benchmark its nested subsets.
        cases = [
            case for case in records
            if case["clue_count"] == max(CLUE_COUNTS)
        ]

        if len({case["base_id"] for case in cases}) != len(cases):
            raise ValueError(f"Duplicate {experiment} base IDs")

        return cases

    if experiment == "thermometer":
        # Keep the six-thermometer record for each base puzzle.
        cases = [
            case for case in records
            if case["thermometer_count"] == 6
        ]
        if len({case["base_id"] for case in cases}) != len(cases):
            raise ValueError("Duplicate thermometer base IDs")
        return cases

    if experiment == "givens":
        return records

    raise ValueError(experiment)


def reference_assignment(case):
    return {
        (r, c): case["solution"][r][c]
        for r in range(9)
        for c in range(9)
    }


def verify_case(case, condition):
    grid = case["puzzle"]
    reference = case["solution"]

    if sum(value != 0 for row in grid for value in row) != case["given_count"]:
        raise ValueError("Given count mismatch")

    if any(
        grid[r][c] not in (0, reference[r][c])
        for r in range(9)
        for c in range(9)
    ):
        raise ValueError("Givens disagree with reference")

    puzzle = build_puzzle(case, condition)
    errors = validate_solution(puzzle, reference_assignment(case))

    if errors:
        raise ValueError(f"Reference violates constraints: {errors}")

    return puzzle


def run_case(experiment, case, condition, extra_count, repeats, uniqueness):
    case_id = case.get("base_id", case["id"])
    row = {field: "" for field in FIELDS}

    row.update({
        "experiment": experiment,
        "id": f"{experiment}__{case_id}__{condition}",        "base_id": case_id,
        "group": case["group"],
        "grid_index": case["grid_index"],
        "pattern_index": case["pattern_index"],
        "given_count": case["given_count"],
        "condition": condition,
        "extra_constraint_count": extra_count,
        "status": "ERROR",
    })

    try:
        puzzle = verify_case(case, condition)
        row["constraint_count"] = len(puzzle.constraints)

        # Instrumented run: collect search and propagation metrics.
        solution, solver = puzzle.solve(instrument=True)

        if solution is None:
            row["status"] = "UNSOLVED"
            return row

        errors = validate_solution(puzzle, solution)
        if errors:
            raise RuntimeError(f"Invalid solution: {errors}")

        row["validation"] = "PASS"
        row["reference_match"] = solution == reference_assignment(case)
        row["search_decisions"] = solver.nodes
        row["backtracks"] = solver.backtracks
        row["propagation_rounds"] = solver.propagation_rounds

        for field in METRIC_FIELDS:
            row[field] = solver.metrics.get(field, "")

        # Uninstrumented runs: use only these for runtime comparisons.
        runtimes = []

        for _ in range(repeats):
            timing_puzzle = build_puzzle(case, condition)

            start = time.perf_counter()
            timing_solution, _ = timing_puzzle.solve(instrument=False)
            elapsed = time.perf_counter() - start

            if timing_solution is None:
                raise RuntimeError("Timing trial found no solution")

            if validate_solution(timing_puzzle, timing_solution):
                raise RuntimeError("Timing trial returned invalid solution")

            runtimes.append(elapsed)

        row["elapsed_seconds"] = statistics.median(runtimes)
        row["min_seconds"] = min(runtimes)
        row["max_seconds"] = max(runtimes)
        row["timing_trials"] = repeats

        # Uniqueness is deliberately measured separately.
        if uniqueness:
            unique_puzzle = build_puzzle(case, condition)

            start = time.perf_counter()
            status, solutions, unique_solver = unique_puzzle.check_uniqueness()
            row["uniqueness_seconds"] = time.perf_counter() - start

            if status not in ("unique", "multiple"):
                raise RuntimeError(f"Unexpected uniqueness status: {status}")

            if not solutions or any(
                validate_solution(unique_puzzle, sol)
                for sol in solutions
            ):
                raise RuntimeError("Invalid uniqueness solutions")

            if status == "unique" and not row["reference_match"]:
                raise RuntimeError("Unique solution differs from reference")

            row["uniqueness"] = status
            row["uniqueness_search_decisions"] = unique_solver.nodes

        row["status"] = "SOLVED"

    except Exception as exc:
        row["status"] = "ERROR"
        row["error"] = f"{type(exc).__name__}: {exc}"

    return row


def summarize(rows):
    print("\n========== CONTROLLED BENCHMARK SUMMARY ==========")

    conditions = sorted(set(row["condition"] for row in rows))

    for condition in conditions:
        subset = [row for row in rows if row["condition"] == condition]
        solved = [row for row in subset if row["status"] == "SOLVED"]

        print(f"\n{condition}")
        print(f"  Trials: {len(subset)}")
        print(f"  Solved: {len(solved)}")
        print(f"  Unique: {sum(r['uniqueness'] == 'unique' for r in solved)}")
        print(f"  Errors: {sum(r['status'] == 'ERROR' for r in subset)}")

        if solved:
            for label, field in [
                ("Median seconds", "elapsed_seconds"),
                ("Median decisions", "search_decisions"),
                ("Median backtracks", "backtracks"),
                ("Median initial eliminations", "initial_candidates_eliminated"),
                ("Median total eliminations", "candidates_eliminated"),
            ]:
                values = [
                    float(row[field])
                    for row in solved
                    if row[field] != ""
                ]
                if values:
                    print(f"  {label}: {statistics.median(values):.6f}")

def replace_with_retry(source, destination, attempts=10, delay=0.5):
    """Handle temporary Windows file locks when saving benchmark results."""
    for attempt in range(attempts):
        try:
            os.replace(source, destination)
            return
        except PermissionError:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)


def stratified_sample(cases, per_stratum, seed):
    """Sample across group and givens count reproducibly."""
    if per_stratum < 1:
        raise ValueError("--stratified must be at least 1")

    groups = {}

    for case in cases:
        key = (case["group"], case["given_count"])
        groups.setdefault(key, []).append(case)

    rng = random.Random(seed)
    selected = []

    for key in sorted(groups):
        population = groups[key]

        if len(population) < per_stratum:
            raise ValueError(
                f"Stratum {key} has only {len(population)} cases"
            )

        selected.extend(
            rng.sample(population, per_stratum)
        )

    return selected


def benchmark_worker(queue, experiment, case, condition,
                     extra_count, repeats, uniqueness):
    try:
        result = run_case(
            experiment,
            case,
            condition,
            extra_count,
            repeats,
            uniqueness,
        )
        queue.put(result)
    except BaseException as exc:
        queue.put({
            "status": "ERROR",
            "error": f"Worker failure: {type(exc).__name__}: {exc}",
        })


def run_case_with_timeout(
    experiment, case, condition, extra_count,
    repeats, uniqueness, timeout,
):
    if timeout is None:
        return run_case(
            experiment, case, condition,
            extra_count, repeats, uniqueness,
        )

    ctx = mp.get_context("spawn")
    queue = ctx.Queue()

    process = ctx.Process(
        target=benchmark_worker,
        args=(
            queue, experiment, case, condition,
            extra_count, repeats, uniqueness,
        ),
    )

    process.start()

    try:
        # The worker sends its result before exiting.
        # Reading with a timeout also avoids a queue deadlock.
        try:
            result = queue.get(timeout=timeout)
        except Exception as exc:
            import queue as queue_module

            if not isinstance(exc, queue_module.Empty):
                raise

            result = None

        if result is not None and "id" in result:
            return result

        row = {field: "" for field in FIELDS}
        case_id = case.get("base_id", case["id"])

        row.update({
            "experiment": experiment,
            "id": f"{experiment}__{case_id}__{condition}",
            "base_id": case_id,
            "group": case["group"],
            "grid_index": case["grid_index"],
            "pattern_index": case["pattern_index"],
            "given_count": case["given_count"],
            "condition": condition,
            "extra_constraint_count": extra_count,
            "status": "ERROR",
            "error": (
                result["error"]
                if result is not None
                else f"Timeout or worker exit after {timeout} seconds"
            ),
        })

        return row

    finally:
        if process.is_alive():
            process.terminate()

        process.join(timeout=5)

        if process.is_alive():
            process.kill()
            process.join()

        queue.close()
        queue.join_thread()

def main():
    parser = argparse.ArgumentParser()

    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--experiment", choices=DATASETS)
    selection.add_argument("--all", action="store_true")

    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--no-uniqueness", action="store_true")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--stratified", type=int, metavar="N")
    parser.add_argument( "--seed",  type=int, default=2026)
    parser.add_argument("--timeout", type=float, default=None)

    args = parser.parse_args()

    if args.full and args.stratified is not None:
        parser.error("--full cannot be combined with --stratified")
    if args.timeout is not None and args.timeout <= 0:
        parser.error("--timeout must be positive")
    if args.repeat < 1:
        parser.error("--repeat must be at least 1")
    if args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.all and args.input is not None:
        parser.error("--input cannot be combined with --all")

    output_path = args.output or Path(
        "output/controlled/controlled_results.csv"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load existing results, preserving completed experiments.
    results = {}

    if output_path.exists():
        with output_path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != FIELDS:
                raise ValueError(
                    "Existing CSV has a different schema. "
                    "Archive or rename it first."
                )

            for row in reader:
                if row["id"] in results:
                    raise ValueError(f"Duplicate result ID: {row['id']}")
                results[row["id"]] = row

    experiments = (
        list(DATASETS)
        if args.all
        else [args.experiment]
    )

    selected_ids = set()

    for experiment in experiments:
        input_path = (
            args.input if args.input is not None
            else DATASETS[experiment]
        )

        with input_path.open(encoding="utf-8") as file:
            records = json.load(file)["experiments"]

        cases = prepare_cases(experiment, records)

        
        if args.stratified is not None:
            cases = stratified_sample(
                cases,
                args.stratified,
                args.seed,
            )
        elif not args.full:
            cases = cases[:args.limit]

        total = sum(
            len(get_conditions(experiment, case))
            for case in cases
        )

        processed = 0

        print(
            f"\n========== {experiment.upper()} ==========",
            flush=True,
        )

        for case in cases:
            for condition, extra_count in get_conditions(
                experiment, case
            ):
                processed += 1

                case_id = case.get("base_id", case["id"])
                result_id = (
                    f"{experiment}__{case_id}__{condition}"
                )

                selected_ids.add(result_id)

                if result_id in results:
                    if (
                        not args.retry_failed
                        or results[result_id]["status"] == "SOLVED"
                    ):
                        continue

                row = run_case_with_timeout(
                    experiment,
                    case,
                    condition,
                    extra_count,
                    args.repeat,
                    not args.no_uniqueness,
                    args.timeout,
                )

                results[result_id] = row

                # Save after each case, allowing interrupted runs
                # to resume without losing completed measurements.
                temporary = output_path.with_suffix(".tmp")

                with temporary.open(
                    "w", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.DictWriter(
                        file, fieldnames=FIELDS
                    )
                    writer.writeheader()
                    writer.writerows(results.values())

                replace_with_retry(temporary, output_path)

                print(
                    f"[{processed}/{total}] {row['id']} | "
                    f"{row['status']} | "
                    f"{row['search_decisions']} decisions | "
                    f"{row['elapsed_seconds']} seconds",
                    flush=True,
                )

                if row["error"]:
                    print(
                        f"  ERROR: {row['error']}",
                        flush=True,
                    )

    summarize([
        row
        for result_id, row in results.items()
        if result_id in selected_ids
    ])

    print(f"\nMaster results: {output_path}")
    print(f"Total stored configurations: {len(results)}")

if __name__ == "__main__":
    main()