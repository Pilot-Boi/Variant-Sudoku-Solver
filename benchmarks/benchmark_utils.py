"""Shared benchmark discovery, measurement, and CSV utilities."""
import csv
import importlib
import pkgutil
import statistics
import time
from pathlib import Path

import puzzles
from sudoku.validator import validate_solution
from benchmarks.ctc_metadata import get_ctc_metadata

TRIALS = 5
BENCHMARK_FIELDNAMES = [
    'puzzle', 'status', 'solutions', 'validation', 'givens', 'constraints',
    'elapsed_seconds', 'min_seconds', 'max_seconds', 'trials',
    'search_decisions', 'solving_method', 'backtracks', 'propagation_rounds',
    'ctc_catalogue_id', 'ctc_title', 'ctc_setter', 'ctc_human_solver',
    'ctc_video_date', 'ctc_video_duration', 'ctc_video_seconds',
    'video_to_solver_ratio',
]
CTC_COMPARISON_FIELDNAMES = [
    'Catalogue ID', 'Puzzle Title', 'Setter', 'Human Solver', 'Video Date',
    'Video Duration', 'Video Seconds', 'Solver Seconds', 'Video/Solver Ratio',
    'Search Decisions', 'Backtracks', 'Propagation Rounds', 'Givens',
    'Constraints', 'Solution Status', 'Validation',
]

def discover_puzzle_modules():
    """Discover puzzle modules recursively, keyed by fully qualified module path."""
    discovered = {}
    for info in pkgutil.walk_packages(puzzles.__path__, prefix="puzzles."):
        if info.ispkg or info.name.rsplit(".", 1)[-1].startswith("_"):
            continue
        module = importlib.import_module(info.name)
        if callable(getattr(module, "create_puzzle", None)):
            discovered[info.name] = module
    return dict(sorted(discovered.items()))


def is_ctc_module(module_name):
    """Support both legacy puzzles.ctc_001 and new puzzles.ctc.ctc_001."""
    parts = module_name.split(".")
    return (len(parts) >= 3 and parts[1] == "ctc") or parts[-1].startswith("ctc_")


def discover_puzzles(category=None):
    """
    Return {puzzle_name: create_puzzle_function}
    for all discovered puzzle modules.
    """
    discovered = {}

    for module_path, module in discover_puzzle_modules().items():
        if category == "generic" and ".generic." not in module_path:
            continue

        if category == "ctc" and not is_ctc_module(module_path):
            continue

        name = getattr(module, "NAME", module_path)

        if name in discovered:
            raise ValueError(f"Duplicate puzzle name: {name}")

        discovered[name] = module.create_puzzle

    return dict(sorted(discovered.items()))


def compute_video_ratio(video_seconds, elapsed_seconds):
    if not video_seconds or not elapsed_seconds or elapsed_seconds < 1e-9:
        return None
    return round(video_seconds / elapsed_seconds, 1)


def ctc_fields(name, elapsed_seconds):
    metadata = get_ctc_metadata(name) or {}
    ratio = compute_video_ratio(metadata.get('video_seconds'), elapsed_seconds)
    return {
        'ctc_catalogue_id': metadata.get('catalogue_id', ''),
        'ctc_title': metadata.get('title', ''),
        'ctc_setter': metadata.get('setter', ''),
        'ctc_human_solver': metadata.get('human_solver', ''),
        'ctc_video_date': metadata.get('video_date', ''),
        'ctc_video_duration': metadata.get('video_duration', ''),
        'ctc_video_seconds': metadata.get('video_seconds', ''),
        'video_to_solver_ratio': '' if ratio is None else ratio,
    }


def benchmark_puzzle(name, create_puzzle, trials=TRIALS):
    if trials < 1:
        raise ValueError('trials must be at least 1')
    runtimes = []
    results = []
    for _ in range(trials):
        puzzle = create_puzzle()
        givens = sum(value != 0 for row in puzzle.grid for value in row)
        constraint_count = len(puzzle.constraints)
        start = time.perf_counter()
        status, solutions, solver = puzzle.check_uniqueness()
        elapsed = time.perf_counter() - start
        validation = 'N/A'
        if solutions:
            errors = [error for solution in solutions
                      for error in validate_solution(puzzle, solution)]
            validation = 'FAIL' if errors else 'PASS'
        runtimes.append(elapsed)
        results.append({
            'status': status, 'solutions': len(solutions),
            'validation': validation, 'givens': givens,
            'constraints': constraint_count, 'search_decisions': solver.nodes,
            'backtracks': solver.backtracks,
            'propagation_rounds': solver.propagation_rounds,
        })
    first = results[0]
    if any(result != first for result in results[1:]):
        raise RuntimeError(f'Inconsistent benchmark results for {name}')
    median = round(statistics.median(runtimes), 6)
    return {
        'puzzle': name, **first,
        'solving_method': ('Propagation Only' if first['search_decisions'] == 0
                           else 'Propagation + Search'),
        'elapsed_seconds': median,
        'min_seconds': round(min(runtimes), 6),
        'max_seconds': round(max(runtimes), 6),
        'trials': trials,
        **ctc_fields(name, median),
    }

def benchmark_first_solution(name, create_puzzle, instrument=False):
    """Benchmark finding one solution without checking uniqueness."""
    puzzle = create_puzzle()

    givens = sum(
        value != 0
        for row in puzzle.grid
        for value in row
    )

    constraint_count = len(puzzle.constraints)

    start = time.perf_counter()
    
    solution, solver = puzzle.solve(instrument=instrument)
    elapsed = time.perf_counter() - start

    if solution is None:
        status = "UNSOLVED"
        validation = "N/A"
    else:
        errors = validate_solution(puzzle, solution)
        validation = "FAIL" if errors else "PASS"
        status = "SOLVED" if not errors else "INVALID"

    result = {
        "puzzle": name,
        "status": status,
        "validation": validation,
        "givens": givens,
        "constraints": constraint_count,
        "elapsed_seconds": round(elapsed, 6),
        "search_decisions": solver.nodes,
        "backtracks": solver.backtracks,
        "propagation_rounds": solver.propagation_rounds,
        "solving_method": (
            "Propagation Only"
            if solver.nodes == 0
            else "Propagation + Search"
        ),
    }

    if instrument:
        result.update({
            key: value
            for key, value in solver.metrics.items()
            if key != "constraint_types"
        })
        result["constraint_types"] = solver.metrics["constraint_types"]

    return result
    
def write_benchmark_csv(results, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=BENCHMARK_FIELDNAMES)
        writer.writeheader()
        writer.writerows(results)
    return path


def write_ctc_comparison(results, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [{
        'Catalogue ID': result['ctc_catalogue_id'],
        'Puzzle Title': result['ctc_title'],
        'Setter': result['ctc_setter'],
        'Human Solver': result['ctc_human_solver'],
        'Video Date': result['ctc_video_date'],
        'Video Duration': result['ctc_video_duration'],
        'Video Seconds': result['ctc_video_seconds'],
        'Solver Seconds': result['elapsed_seconds'],
        'Video/Solver Ratio': result['video_to_solver_ratio'],
        'Search Decisions': result['search_decisions'],
        'Backtracks': result['backtracks'],
        'Propagation Rounds': result['propagation_rounds'],
        'Givens': result['givens'],
        'Constraints': result['constraints'],
        'Solution Status': result['status'],
        'Validation': result['validation'],
    } for result in results if result['ctc_catalogue_id'] != '']
    with path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=CTC_COMPARISON_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    return path


def print_result(result):
    print(f"  {result['status']} | {result['elapsed_seconds']:.4f}s | "
          f"{result['search_decisions']} decisions | "
          f"{result['backtracks']} backtracks | {result['solving_method']}")
    print(f"  {result['givens']} givens | {result['constraints']} constraints")
