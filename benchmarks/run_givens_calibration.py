"""Calibrate the number of givens for controlled Sudoku experiments.

Run from the project root: python -m benchmarks.run_givens_calibration
"""
import csv
import json
import statistics
from pathlib import Path
from time import perf_counter

from sudoku.puzzle import SudokuPuzzle

INPUT_FILE = Path('puzzles/controlled/givens_experiment.json')
OUTPUT_FILE = Path('output/controlled/givens_calibration.csv')
SUMMARY_FILE = Path('output/controlled/givens_calibration_summary.csv')
TRIALS = 3
CHECK_UNIQUENESS = True

FIELDS = [
    'id', 'group', 'grid_index', 'pattern_index', 'given_count',
    'status', 'first_solution_matches_reference', 'elapsed_seconds',
    'min_seconds', 'max_seconds', 'trials', 'search_decisions',
    'backtracks', 'propagation_rounds', 'candidates_eliminated',
    'initial_candidates_eliminated', 'constraint_evaluations',
    'constraint_reductions', 'constraint_contradictions',
    'validation_contradictions', 'max_search_depth', 'failed_branches',
    'total_propagation_seconds', 'initial_propagation_seconds',
    'uniqueness_seconds', 'uniqueness_search_decisions',
]


def is_valid_standard_solution(solution, givens):
    if solution is None or len(solution) != 81:
        return False
    digits = set(range(1, 10))
    for r in range(9):
        if {solution[(r, c)] for c in range(9)} != digits:
            return False
    for c in range(9):
        if {solution[(r, c)] for r in range(9)} != digits:
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if {solution[(r, c)] for r in range(br, br + 3)
                for c in range(bc, bc + 3)} != digits:
                return False
    return all(not givens[r][c] or solution[(r, c)] == givens[r][c]
               for r in range(9) for c in range(9))


def benchmark_case(case):
    grid = case['puzzle']
    reference = case['solution']
    actual_givens = sum(v != 0 for row in grid for v in row)
    if actual_givens != case['given_count']:
        raise ValueError(f"Wrong given count for {case['id']}")
    if any(grid[r][c] not in (0, reference[r][c])
           for r in range(9) for c in range(9)):
        raise ValueError(f"Givens disagree with reference for {case['id']}")

    times = []
    first_solver = None
    first_solution = None
    for trial in range(TRIALS):
        puzzle = SudokuPuzzle(grid)  # Standard constraints only.
        start = perf_counter()
        solution, solver = puzzle.solve(instrument=(trial == 0))
        elapsed = perf_counter() - start
        if not is_valid_standard_solution(solution, grid):
            raise RuntimeError(f"Invalid first solution for {case['id']}")
        times.append(elapsed)
        if trial == 0:
            first_solver = solver
            first_solution = solution

    # Timing includes instrumentation in the first trial only; use the
    # uninstrumented trials for comparable runtime figures when available.
    runtime_trials = times[1:] if TRIALS > 1 else times
    metrics = first_solver.metrics
    row = {
        'id': case['id'],
        'group': case['group'],
        'grid_index': case['grid_index'],
        'pattern_index': case['pattern_index'],
        'given_count': case['given_count'],
        'status': 'not_checked',
        'first_solution_matches_reference': all(
            first_solution[(r, c)] == reference[r][c]
            for r in range(9) for c in range(9)
        ),
        'elapsed_seconds': statistics.median(runtime_trials),
        'min_seconds': min(runtime_trials),
        'max_seconds': max(runtime_trials),
        'trials': len(runtime_trials),
        'search_decisions': first_solver.nodes,
        'backtracks': first_solver.backtracks,
        'propagation_rounds': first_solver.propagation_rounds,
        'uniqueness_seconds': '',
        'uniqueness_search_decisions': '',
    }
    for key in (
        'candidates_eliminated', 'initial_candidates_eliminated',
        'constraint_evaluations', 'constraint_reductions',
        'constraint_contradictions', 'validation_contradictions',
        'max_search_depth', 'failed_branches',
        'total_propagation_seconds', 'initial_propagation_seconds',
    ):
        row[key] = metrics[key]

    if CHECK_UNIQUENESS:
        puzzle = SudokuPuzzle(grid)
        start = perf_counter()
        status, solutions, uniqueness_solver = puzzle.check_uniqueness()
        row['uniqueness_seconds'] = perf_counter() - start
        row['uniqueness_search_decisions'] = uniqueness_solver.nodes
        row['status'] = status
        if status == 'none' or not all(
            is_valid_standard_solution(sol, grid) for sol in solutions
        ):
            raise RuntimeError(f"Uniqueness validation failed for {case['id']}")
        if status == 'unique' and not row['first_solution_matches_reference']:
            raise RuntimeError(f"Unique solution differs from reference: {case['id']}")
    return row


def write_summary(rows):
    fields = [
        'group', 'given_count', 'puzzles', 'unique', 'multiple',
        'propagation_only', 'median_seconds', 'median_decisions',
        'median_backtracks', 'median_candidates_eliminated',
    ]
    grouped = {}
    for row in rows:
        grouped.setdefault((row['group'], row['given_count']), []).append(row)
    with SUMMARY_FILE.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for (group, count), subset in sorted(grouped.items()):
            writer.writerow({
                'group': group, 'given_count': count, 'puzzles': len(subset),
                'unique': sum(r['status'] == 'unique' for r in subset),
                'multiple': sum(r['status'] == 'multiple' for r in subset),
                'propagation_only': sum(r['search_decisions'] == 0 for r in subset),
                'median_seconds': statistics.median(r['elapsed_seconds'] for r in subset),
                'median_decisions': statistics.median(r['search_decisions'] for r in subset),
                'median_backtracks': statistics.median(r['backtracks'] for r in subset),
                'median_candidates_eliminated': statistics.median(
                    r['candidates_eliminated'] for r in subset
                ),
            })


def main():
    with INPUT_FILE.open('r', encoding='utf-8') as file:
        data = json.load(file)
    cases = data['experiments']
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    completed = []
    if OUTPUT_FILE.exists():
        with OUTPUT_FILE.open('r', newline='', encoding='utf-8') as file:
            completed = list(csv.DictReader(file))
        print(f'Resuming: {len(completed)} existing results')
    done_ids = {r['id'] for r in completed}

    with OUTPUT_FILE.open('a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not completed:
            writer.writeheader()
        for index, case in enumerate(cases, start=1):
            if case['id'] in done_ids:
                continue
            row = benchmark_case(case)
            writer.writerow(row)
            file.flush()  # Save each result in case the run is interrupted.
            completed.append(row)
            print(f"[{index}/{len(cases)}] {row['id']} | {row['status']} | "
                  f"{row['search_decisions']} decisions | "
                  f"{row['elapsed_seconds']:.4f}s", flush=True)

    # Convert persisted string columns when resuming.
    for row in completed:
        for key in ('given_count', 'search_decisions', 'backtracks',
                    'candidates_eliminated'):
            row[key] = float(row[key])
        row['elapsed_seconds'] = float(row['elapsed_seconds'])
    write_summary(completed)
    print(f'\nDetailed results: {OUTPUT_FILE}')
    print(f'Summary: {SUMMARY_FILE}')


if __name__ == '__main__':
    main()
