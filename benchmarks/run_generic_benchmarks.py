"""
    Benchmark non-CTC sample puzzles independently of CTC puzzles.
    
    python -m benchmarks.run_generic_benchmarks
"""
import argparse
from pathlib import Path
from benchmarks.benchmark_utils import (
    benchmark_puzzle, discover_puzzle_modules, is_ctc_module,
    print_result, write_benchmark_csv,
)

OUTPUT_FILE = Path('output/generic_benchmark_results.csv')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trials', type=int, default=5)
    args = parser.parse_args(argv)
    if args.trials < 1:
        parser.error('--trials must be at least 1')

    modules = {
        key: module for key, module in discover_puzzle_modules().items()
        if not is_ctc_module(key)
    }
    print(f'Discovered {len(modules)} generic puzzles.\n')
    results = []
    for key, module in modules.items():
        name = getattr(module, 'NAME', key)
        print(f'Benchmarking {name}...')
        result = benchmark_puzzle(name, module.create_puzzle, trials=args.trials)
        results.append(result)
        print_result(result)
    write_benchmark_csv(results, OUTPUT_FILE)
    print(f'\nResults saved to {OUTPUT_FILE}')


if __name__ == '__main__':
    main()
