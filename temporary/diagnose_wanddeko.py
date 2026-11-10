"""
Diagnose Wanddeko (puzzles/ctc_002.py) solver behavior.

Measures solve/uniqueness timing, search statistics, and
optional cProfile hotspots across fresh puzzle instances.
The embedded solution is only used to verify results,
never to guide the search.

Usage:
    python diagnose_wanddeko.py
    python diagnose_wanddeko.py --uniqueness --runs 5
    python diagnose_wanddeko.py --profile --top 30
"""

import argparse
import cProfile
import io
import pstats
import statistics
import sys
import time
from pathlib import Path

from puzzles.ctc.ctc_002 import SOLUTION, create_puzzle
from sudoku.validator import validate_solution


def expected_solution():
    """The embedded solution as a cell assignment dict."""
    return {
        (r, c): int(SOLUTION[r * 9 + c])
        for r in range(9)
        for c in range(9)
    }


def show_profile(profiler, limit):
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).strip_dirs()
    stats.sort_stats('cumtime').print_stats(limit)
    print('\nTOP FUNCTIONS BY CUMULATIVE TIME')
    print(stream.getvalue())
    stream = io.StringIO()
    stats.stream = stream
    stats.sort_stats('tottime').print_stats(limit)
    print('TOP FUNCTIONS BY EXCLUSIVE TIME')
    print(stream.getvalue())


def run_once(index, mode, profile, limit, save_profile):
    puzzle = create_puzzle()  # Fresh instance for every run.
    profiler = cProfile.Profile() if profile else None
    if profiler:
        profiler.enable()
    start = time.perf_counter()
    try:
        if mode == 'uniqueness':
            status, solutions, solver = puzzle.check_uniqueness()
            solution = solutions[0] if solutions else None
        else:
            solution, solver = puzzle.solve()
            status = 'found' if solution is not None else 'none'
    finally:
        elapsed = time.perf_counter() - start
        if profiler:
            profiler.disable()

    print(f'\nRUN {index} — {mode.upper()}')
    print(f'Elapsed:           {elapsed:.4f}s')
    print(f'Status:            {status}')
    print(f'Decisions/nodes:   {getattr(solver, "nodes", "unavailable")}')
    print(f'Backtracks:        {getattr(solver, "backtracks", "unavailable")}')
    print(f'Propagation rounds:{getattr(solver, "propagation_rounds", "unavailable"):>10}')
    if solution is not None:
        errors = validate_solution(puzzle, solution)
        print(f'Validation:        {"PASS" if not errors else "FAIL"}')
        if errors:
            print(f'Validation errors: {errors[:5]}')
        print(f'Matches embedded:  {solution == expected_solution()}')
    else:
        print('No solution returned.')
    if mode == 'uniqueness':
        print(f'Solutions returned: {len(solutions)}')
        if len(solutions) > 1:
            print('WARNING: More than one solution found.')

    if profiler:
        if save_profile:
            out = Path(save_profile)
            if index > 1:
                out = out.with_name(f'{out.stem}_run{index}{out.suffix or ".prof"}')
            profiler.dump_stats(str(out))
            print(f'Raw profile saved: {out}')
        show_profile(profiler, limit)
    return elapsed, getattr(solver, 'nodes', None), getattr(solver, 'backtracks', None)


def main():
    parser = argparse.ArgumentParser(description='Diagnose Wanddeko search and hotspots.')
    parser.add_argument('--runs', type=int, default=3, help='Independent runs (default: 3).')
    parser.add_argument('--uniqueness', action='store_true', help='Profile full uniqueness check instead of first solution.')
    parser.add_argument('--profile', action='store_true', help='Enable cProfile (adds overhead; do not use profiled times as benchmarks).')
    parser.add_argument('--top', type=int, default=20, help='Number of profiler functions to display.')
    parser.add_argument('--save-profile', metavar='PATH', help='Optional raw .prof output file.')
    args = parser.parse_args()
    if args.runs < 1 or args.top < 1:
        parser.error('--runs and --top must be positive')
    if args.save_profile and not args.profile:
        parser.error('--save-profile requires --profile')

    mode = 'uniqueness' if args.uniqueness else 'first solution'
    print('WANDDEKO SOLVER DIAGNOSTICS')
    print(f'Mode: {mode} | Runs: {args.runs} | cProfile: {args.profile}')
    print(f'Python: {sys.version.split()[0]}')
    print('NOTE: This script never uses the embedded solution to guide search.')
    print('NOTE: cProfile can significantly slow down execution.')

    results = []
    try:
        for i in range(1, args.runs + 1):
            results.append(run_once(i, 'uniqueness' if args.uniqueness else 'solve', args.profile, args.top, args.save_profile))
    except KeyboardInterrupt:
        print('\nInterrupted. Completed runs are shown below.')
    if not results:
        return
    times = [row[0] for row in results]
    print('\nSUMMARY')
    print(f'Median elapsed: {statistics.median(times):.4f}s')
    print(f'Min / max:      {min(times):.4f}s / {max(times):.4f}s')
    for label, idx in [('Decisions', 1), ('Backtracks', 2)]:
        values = [row[idx] for row in results]
        if all(isinstance(x, int) for x in values):
            print(f'{label} across runs: {values}')
            if len(set(values)) != 1:
                print(f'  WARNING: {label.lower()} varied across identical fresh runs.')
    print('Interpretation: stable high search counts suggest repeatable search work;')
    print('large time variation at fixed counts suggests runtime/environment effects.')
    print('Inspect cumulative/exclusive profiler hotspots for avoidable overhead.')


if __name__ == '__main__':
    main()