import csv
import time
import statistics
import importlib
import pkgutil
import puzzles
from pathlib import Path

from sudoku.validator import validate_solution

TRIALS = 5

OUTPUT_FILE = Path("output/benchmark_results.csv")

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

    return {
        "puzzle": name,
        **first,
        "solving_method": classify_solving_method(
            first["search_decisions"]
        ),
        "elapsed_seconds": round(statistics.median(runtimes), 6),
        "min_seconds": round(min(runtimes), 6),
        "max_seconds": round(max(runtimes), 6),
        "trials": TRIALS,
    }


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

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
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
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()