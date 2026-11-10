"""
    Benchmark CTC puzzles, optionally selecting one or more module names.

    ALL CTC PUZZLES: python -m benchmarks.run_ctc_benchmarks
    TARGETED RUN: python -m benchmarks.run_ctc_benchmarks --puzzle ctc_005
    TARGETED RUN ONE TRIAL: python -m benchmarks.run_ctc_benchmarks --puzzle ctc_005 --trials 1
"""
import argparse
from pathlib import Path
from benchmarks.benchmark_utils import (
    benchmark_puzzle, discover_puzzle_modules, is_ctc_module,
    print_result, write_benchmark_csv, write_ctc_comparison,
)
from benchmarks.ctc_metadata import seconds_to_duration

OUTPUT_FILE = Path('output/ctc_benchmark_results.csv')
CTC_OUTPUT_FILE = Path('output/ctc_comparison.csv')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--puzzle', action='append', metavar='ctc_005',
                        help='Select a CTC module; repeat to select multiple')
    parser.add_argument('--trials', type=int, default=5)
    args = parser.parse_args(argv)
    if args.trials < 1:
        parser.error('--trials must be at least 1')
    all_modules = {
        key: module for key, module in discover_puzzle_modules().items()
        if is_ctc_module(key)
    }
    # Accept short names (ctc_005) and full paths (puzzles.ctc.ctc_005).
    short_names = {}
    for path in all_modules:
        short = path.rsplit(".", 1)[-1]
        if short in short_names:
            parser.error(f"Duplicate CTC module basename: {short}")
        short_names[short] = path
    modules = all_modules
    if args.puzzle:
        selected = {}
        for requested in args.puzzle:
            path = requested if requested in all_modules else short_names.get(requested)
            if path is None:
                parser.error(f"Unknown CTC puzzle module: {requested}")
            selected[path] = all_modules[path]
        modules = dict(sorted(selected.items()))
    print(f'Discovered {len(modules)} selected CTC puzzles.\n')
    results = []
    for key, module in modules.items():
        name = getattr(module, 'NAME', key)
        print(f'Benchmarking {name}...')
        result = benchmark_puzzle(name, module.create_puzzle, trials=args.trials)
        results.append(result)
        print_result(result)
        if result['ctc_video_seconds'] != '':
            ratio = result['video_to_solver_ratio']
            ratio_text = f'{ratio:.0f}x' if ratio != '' else 'n/a'
            print(f"  CTC video: {seconds_to_duration(result['ctc_video_seconds'])} | "
                  f'Video/solver ratio: {ratio_text}')

    # A targeted run must not overwrite the full-collection CSVs.
    if args.puzzle:
        stem = '_'.join(sorted(key.rsplit('.', 1)[-1] for key in modules))
        output = Path('output') / f'ctc_benchmark_{stem}.csv'
        comparison = Path('output') / f'ctc_comparison_{stem}.csv'
    else:
        output = OUTPUT_FILE
        comparison = CTC_OUTPUT_FILE
    write_benchmark_csv(results, output)
    write_ctc_comparison(results, comparison)
    print(f'\nResults saved to {output}')
    print(f'CTC comparison saved to {comparison}')


if __name__ == '__main__':
    main()
