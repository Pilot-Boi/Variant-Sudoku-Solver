import csv
import time
import statistics
import importlib
import pkgutil
import puzzles
from pathlib import Path

from sudoku.validator import validate_solution
from benchmarks.ctc_metadata import (
    get_ctc_metadata,
    seconds_to_duration,
)

TRIALS = 5

OUTPUT_FILE = Path("output/benchmark_results.csv")
CTC_OUTPUT_FILE = Path("output/ctc_comparison.csv")

BENCHMARK_FIELDNAMES = [
    "puzzle",
    "status",
    "solutions",
    "validation",
    "givens",
    "constraints",
    "elapsed_seconds",
    "min_seconds",
    "max_seconds",
    "trials",
    "search_decisions",
    "solving_method",
    "backtracks",
    "propagation_rounds",
    "ctc_catalogue_id",
    "ctc_title",
    "ctc_setter",
    "ctc_human_solver",
    "ctc_video_date",
    "ctc_video_duration",
    "ctc_video_seconds",
    "video_to_solver_ratio",
]

CTC_COMPARISON_FIELDNAMES = [
    "Catalogue ID",
    "Puzzle Title",
    "Setter",
    "Human Solver",
    "Video Date",
    "Video Duration",
    "Video Seconds",
    "Solver Seconds",
    "Video/Solver Ratio",
    "Search Decisions",
    "Backtracks",
    "Propagation Rounds",
    "Givens",
    "Constraints",
    "Solution Status",
    "Validation",
]

def discover_puzzles():
    """
    Discover puzzle modules exposing create_puzzle().

    Returns a dictionary:
        {puzzle_name: create_puzzle_function}
    """
    discovered = {}

    for module_info in pkgutil.iter_modules(puzzles.__path__):
        if module_info.ispkg:
            continue

        module_name = module_info.name

        if module_name.startswith("_"):
            continue

        module = importlib.import_module(
            f"puzzles.{module_name}"
        )

        create_puzzle = getattr(module, "create_puzzle", None)

        if not callable(create_puzzle):
            continue

        name = getattr(module, "NAME", module_name)

        if name in discovered:
            raise ValueError(
                f"Duplicate puzzle name: {name}"
            )

        discovered[name] = create_puzzle

    return dict(sorted(discovered.items()))

def classify_solving_method(nodes):
    if nodes == 0:
        return "Propagation Only"

    return "Propagation + Search"


def compute_video_ratio(video_seconds, elapsed_seconds):
    """
    Video-to-solver duration ratio.

    This compares the published video length with the
    solver's median runtime. It is not a literal
    human-solving-speed ratio. Returns None when the
    ratio cannot be computed safely.
    """
    if not video_seconds:
        return None

    if not elapsed_seconds or elapsed_seconds < 1e-9:
        return None

    return round(video_seconds / elapsed_seconds, 1)


def ctc_fields(name, elapsed_seconds):
    """
    CTC metadata columns for one benchmark result.

    Non-CTC puzzles and missing metadata fields
    produce blank values.
    """
    metadata = get_ctc_metadata(name)

    if metadata is None:
        metadata = {}

    ratio = compute_video_ratio(
        metadata.get("video_seconds"),
        elapsed_seconds,
    )

    return {
        "ctc_catalogue_id": metadata.get("catalogue_id", ""),
        "ctc_title": metadata.get("title", ""),
        "ctc_setter": metadata.get("setter", ""),
        "ctc_human_solver": metadata.get("human_solver", ""),
        "ctc_video_date": metadata.get("video_date", ""),
        "ctc_video_duration": metadata.get("video_duration", ""),
        "ctc_video_seconds": metadata.get("video_seconds", ""),
        "video_to_solver_ratio": (
            "" if ratio is None else ratio
        ),
    }

def benchmark_puzzle(name, create_puzzle):
    runtimes = []
    results = []

    for _ in range(TRIALS):
        puzzle = create_puzzle()
        
        givens = sum(
            value != 0
            for row in puzzle.grid
            for value in row
        )

        constraint_count = len(puzzle.constraints)

        start = time.perf_counter()
        status, solutions, solver = puzzle.check_uniqueness()
        elapsed = time.perf_counter() - start

        validation = "N/A"

        if solutions:
            errors = []
            for solution in solutions:
                errors.extend(validate_solution(puzzle, solution))

            validation = "PASS" if not errors else "FAIL"

        runtimes.append(elapsed)

        results.append({
            "status": status,
            "solutions": len(solutions),
            "validation": validation,
            "givens": givens,
            "constraints": constraint_count,
            "search_decisions": solver.nodes,
            "backtracks": solver.backtracks,
            "propagation_rounds": solver.propagation_rounds,
        })

    first = results[0]

    # Ensure repeated runs produce consistent results.
    if any(result != first for result in results[1:]):
        raise RuntimeError(
            f"Inconsistent benchmark results for {name}"
        )

    elapsed_median = round(statistics.median(runtimes), 6)

    return {
        "puzzle": name,
        **first,
        "solving_method": classify_solving_method(
            first["search_decisions"]
        ),
        "elapsed_seconds": elapsed_median,
        "min_seconds": round(min(runtimes), 6),
        "max_seconds": round(max(runtimes), 6),
        "trials": TRIALS,
        **ctc_fields(name, elapsed_median),
    }


def write_benchmark_csv(results, path=OUTPUT_FILE):
    """Write the full benchmark results CSV."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=BENCHMARK_FIELDNAMES,
        )

        writer.writeheader()
        writer.writerows(results)

    return path


def write_ctc_comparison(results, path=CTC_OUTPUT_FILE):
    """
    Write the human-versus-computer comparison CSV.

    Reuses existing benchmark results; nothing is
    solved again. Puzzles without CTC metadata are
    omitted. With no CTC puzzles, only the header
    row is written.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows = [
        {
            "Catalogue ID": result["ctc_catalogue_id"],
            "Puzzle Title": result["ctc_title"],
            "Setter": result["ctc_setter"],
            "Human Solver": result["ctc_human_solver"],
            "Video Date": result["ctc_video_date"],
            "Video Duration": result["ctc_video_duration"],
            "Video Seconds": result["ctc_video_seconds"],
            "Solver Seconds": result["elapsed_seconds"],
            "Video/Solver Ratio": result["video_to_solver_ratio"],
            "Search Decisions": result["search_decisions"],
            "Backtracks": result["backtracks"],
            "Propagation Rounds": result["propagation_rounds"],
            "Givens": result["givens"],
            "Constraints": result["constraints"],
            "Solution Status": result["status"],
            "Validation": result["validation"],
        }
        for result in results
        if result["ctc_catalogue_id"] != ""
    ]

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=CTC_COMPARISON_FIELDNAMES,
        )

        writer.writeheader()
        writer.writerows(rows)

    return path


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    puzzle_registry = discover_puzzles()

    print(f"Discovered {len(puzzle_registry)} puzzles.\n")

    results = []

    for name, create_puzzle in puzzle_registry.items():
        print(f"Benchmarking {name}...")

        result = benchmark_puzzle(name, create_puzzle)
        results.append(result)

        print(
            f"  {result['status']} | "
            f"{result['elapsed_seconds']:.4f}s | "
            f"{result['search_decisions']} decisions | "
            f"{result['backtracks']} backtracks | "
            f"{result['solving_method']}"
        )
        
        print(
            f"  {result['givens']} givens | "
            f"{result['constraints']} constraints"
        )

        if result["ctc_video_seconds"] != "":
            ratio = result["video_to_solver_ratio"]

            ratio_text = (
                f"{ratio:.0f}x" if ratio != "" else "n/a"
            )

            video_text = seconds_to_duration(
                result["ctc_video_seconds"]
            )

            print(
                f"  CTC video: {video_text} | "
                f"Video/solver ratio: {ratio_text}"
            )

    write_benchmark_csv(results)
    write_ctc_comparison(results)

    print(f"\nResults saved to {OUTPUT_FILE}")
    print(f"CTC comparison saved to {CTC_OUTPUT_FILE}")


if __name__ == "__main__":
    main()