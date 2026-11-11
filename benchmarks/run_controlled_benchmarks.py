"""Benchmark the additional variant rule against the Standard-only calibration.

Run from the project root:
    python -m benchmarks.run_controlled_benchmarks

Requires puzzles/controlled/givens_experiment.json and the previously generated
output/controlled/givens_calibration.csv. Results are resumable.
"""

import csv
import json
import statistics
from pathlib import Path
from time import perf_counter

from sudoku.puzzle import SudokuPuzzle

INPUT_FILE = Path('puzzles/controlled/givens_experiment.json')
BASELINE_FILE = Path('output/controlled/givens_calibration.csv')
OUTPUT_FILE = Path('output/controlled/controlled_variant_results.csv')
SUMMARY_FILE = Path('output/controlled/controlled_variant_summary.csv')
TRIALS = 3  # One instrumented trial + two uninstrumented timing trials.
CHECK_UNIQUENESS = True

METRIC_FIELDS = [
    'search_decisions', 'backtracks', 'propagation_rounds',
    'candidates_eliminated', 'initial_candidates_eliminated',
    'constraint_evaluations', 'constraint_reductions',
    'constraint_contradictions', 'validation_contradictions',
    'max_search_depth', 'failed_branches',
    'total_propagation_seconds', 'initial_propagation_seconds',
]
FIELDS = [
    'id', 'group', 'grid_index', 'pattern_index', 'given_count',
    'variant', 'constraint_count', 'status', 'first_solution_matches_reference',
    'elapsed_seconds', 'min_seconds', 'max_seconds', 'trials',
    *METRIC_FIELDS, 'uniqueness_seconds', 'uniqueness_search_decisions',
    'baseline_status', 'baseline_elapsed_seconds',
    'baseline_search_decisions', 'baseline_backtracks',
    'baseline_first_solution_matches_reference',
    'decision_reduction', 'backtrack_reduction', 'runtime_change_seconds',
]


def add_variant(puzzle, rules):
    enabled = [name for name in ('diagonal', 'anti_knight', 'anti_king')
               if rules.get(name, False)]
    if not rules.get('standard', False) or len(enabled) > 1:
        raise ValueError(f'Expected Standard plus at most one variant: {rules}')
    if enabled:
        getattr(puzzle, f'add_{enabled[0]}_constraints')()
    return enabled[0] if enabled else 'standard'


def validate_solution(solution, givens, reference, rules):
    if solution is None or len(solution) != 81:
        return False
    digits = set(range(1, 10))
    if any({solution[r, c] for c in range(9)} != digits for r in range(9)):
        return False
    if any({solution[r, c] for r in range(9)} != digits for c in range(9)):
        return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if {solution[r, c] for r in range(br, br + 3)
                for c in range(bc, bc + 3)} != digits:
                return False
    if any(givens[r][c] and solution[r, c] != givens[r][c]
           for r in range(9) for c in range(9)):
        return False
    if rules.get('diagonal'):
        if {solution[i, i] for i in range(9)} != digits:
            return False
        if {solution[i, 8-i] for i in range(9)} != digits:
            return False
    for r in range(9):
        for c in range(9):
            if rules.get('anti_king'):
                for dr, dc in ((1, -1), (1, 1)):
                    rr, cc = r + dr, c + dc
                    if rr < 9 and 0 <= cc < 9 and solution[r, c] == solution[rr, cc]:
                        return False
            if rules.get('anti_knight'):
                for dr, dc in ((1, -2), (1, 2), (2, -1), (2, 1)):
                    rr, cc = r + dr, c + dc
                    if rr < 9 and 0 <= cc < 9 and solution[r, c] == solution[rr, cc]:
                        return False
    return True


def benchmark_case(case, baseline):
    grid = case['puzzle']
    reference = case['solution']
    rules = case['reference_rules']
    if sum(v != 0 for row in grid for v in row) != case['given_count']:
        raise ValueError(f'Given count mismatch: {case["id"]}')
    if any(grid[r][c] not in (0, reference[r][c])
           for r in range(9) for c in range(9)):
        raise ValueError(f'Givens disagree with reference: {case["id"]}')
    expected = {(r, c): reference[r][c] for r in range(9) for c in range(9)}
    if not validate_solution(expected, grid, reference, rules):
        raise ValueError(f'Reference violates its variant rules: {case["id"]}')

    runtimes = []
    first_solver = None
    first_solution = None
    variant = None
    constraint_count = None
    for trial in range(TRIALS):
        puzzle = SudokuPuzzle(grid)
        variant = add_variant(puzzle, rules)
        constraint_count = len(puzzle.constraints)
        start = perf_counter()
        solution, solver = puzzle.solve(instrument=(trial == 0))
        elapsed = perf_counter() - start
        if not validate_solution(solution, grid, reference, rules):
            raise RuntimeError(f'Invalid variant solution: {case["id"]}')
        runtimes.append(elapsed)
        if trial == 0:
            first_solver, first_solution = solver, solution

    runtime_trials = runtimes[1:] if TRIALS > 1 else runtimes
    row = {
        'id': case['id'], 'group': case['group'],
        'grid_index': case['grid_index'], 'pattern_index': case['pattern_index'],
        'given_count': case['given_count'], 'variant': variant,
        'constraint_count': constraint_count, 'status': 'not_checked',
        'first_solution_matches_reference': first_solution == expected,
        'elapsed_seconds': statistics.median(runtime_trials),
        'min_seconds': min(runtime_trials), 'max_seconds': max(runtime_trials),
        'trials': len(runtime_trials),
        'uniqueness_seconds': '', 'uniqueness_search_decisions': '',
        'baseline_status': baseline['status'],
        'baseline_elapsed_seconds': float(baseline['elapsed_seconds']),
        'baseline_search_decisions': int(float(baseline['search_decisions'])),
        'baseline_backtracks': int(float(baseline['backtracks'])),
        'baseline_first_solution_matches_reference': baseline['first_solution_matches_reference'],
    }
    row.update({key: first_solver.metrics[key] if key in first_solver.metrics
                else getattr(first_solver, 'nodes' if key == 'search_decisions'
                             else key) for key in METRIC_FIELDS})
    row['search_decisions'] = first_solver.nodes
    row['backtracks'] = first_solver.backtracks
    row['propagation_rounds'] = first_solver.propagation_rounds
    row['decision_reduction'] = row['baseline_search_decisions'] - row['search_decisions']
    row['backtrack_reduction'] = row['baseline_backtracks'] - row['backtracks']
    row['runtime_change_seconds'] = row['elapsed_seconds'] - row['baseline_elapsed_seconds']

    if CHECK_UNIQUENESS:
        puzzle = SudokuPuzzle(grid)
        add_variant(puzzle, rules)
        start = perf_counter()
        status, solutions, solver = puzzle.check_uniqueness()
        row['uniqueness_seconds'] = perf_counter() - start
        row['uniqueness_search_decisions'] = solver.nodes
        row['status'] = status
        if status == 'none' or not all(validate_solution(sol, grid, reference, rules)
                                       for sol in solutions):
            raise RuntimeError(f'Invalid uniqueness result: {case["id"]}')
        if status == 'unique' and not row['first_solution_matches_reference']:
            raise RuntimeError(f'Unique solution differs from reference: {case["id"]}')
    return row


def write_summary(rows):
    groups = {}
    for row in rows:
        groups.setdefault((row['group'], int(float(row['given_count']))), []).append(row)
    fields = [
        'group', 'given_count', 'puzzles', 'unique', 'multiple',
        'baseline_unique', 'baseline_multiple', 'newly_unique',
        'variant_reference_matches', 'baseline_reference_matches',
        'variant_propagation_only', 'baseline_propagation_only',
        'median_variant_seconds', 'median_baseline_seconds',
        'median_variant_decisions', 'median_baseline_decisions',
        'median_decision_reduction', 'median_variant_backtracks',
        'median_baseline_backtracks', 'median_candidate_eliminations',
    ]
    with SUMMARY_FILE.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for (group, count), subset in sorted(groups.items()):
            def med(key):
                return statistics.median(float(r[key]) for r in subset)
            def yes(value):
                return str(value).lower() == 'true'
            writer.writerow({
                'group': group, 'given_count': count, 'puzzles': len(subset),
                'unique': sum(r['status'] == 'unique' for r in subset),
                'multiple': sum(r['status'] == 'multiple' for r in subset),
                'baseline_unique': sum(r['baseline_status'] == 'unique' for r in subset),
                'baseline_multiple': sum(r['baseline_status'] == 'multiple' for r in subset),
                'newly_unique': sum(r['baseline_status'] == 'multiple' and
                                    r['status'] == 'unique' for r in subset),
                'variant_reference_matches': sum(yes(r['first_solution_matches_reference']) for r in subset),
                'baseline_reference_matches': sum(yes(r['baseline_first_solution_matches_reference']) for r in subset),
                'variant_propagation_only': sum(float(r['search_decisions']) == 0 for r in subset),
                'baseline_propagation_only': sum(float(r['baseline_search_decisions']) == 0 for r in subset),
                'median_variant_seconds': med('elapsed_seconds'),
                'median_baseline_seconds': med('baseline_elapsed_seconds'),
                'median_variant_decisions': med('search_decisions'),
                'median_baseline_decisions': med('baseline_search_decisions'),
                'median_decision_reduction': med('decision_reduction'),
                'median_variant_backtracks': med('backtracks'),
                'median_baseline_backtracks': med('baseline_backtracks'),
                'median_candidate_eliminations': med('candidates_eliminated'),
            })


def main():
    with INPUT_FILE.open('r', encoding='utf-8') as file:
        cases = json.load(file)['experiments']
    with BASELINE_FILE.open('r', newline='', encoding='utf-8') as file:
        baseline = {row['id']: row for row in csv.DictReader(file)}
    if len(baseline) != len(cases) or any(c['id'] not in baseline for c in cases):
        raise ValueError('Baseline CSV must contain exactly the experiment case IDs.')
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    completed = []
    if OUTPUT_FILE.exists():
        with OUTPUT_FILE.open('r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDS:
                raise ValueError('Existing output CSV schema differs; archive it before rerunning.')
            completed = list(reader)
        print(f'Resuming: {len(completed)} results already saved.')
    done = {row['id'] for row in completed}
    with OUTPUT_FILE.open('a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not completed:
            writer.writeheader()
        for index, case in enumerate(cases, start=1):
            if case['id'] in done:
                continue
            row = benchmark_case(case, baseline[case['id']])
            writer.writerow(row)
            file.flush()
            completed.append(row)
            print(f'[{index}/{len(cases)}] {row["id"]} | {row["variant"]} | '
                  f'{row["status"]} | {row["search_decisions"]} decisions '
                  f'(baseline {row["baseline_search_decisions"]})', flush=True)
    write_summary(completed)
    print(f'\nDetailed results: {OUTPUT_FILE}\nSummary: {SUMMARY_FILE}')


if __name__ == '__main__':
    main()
