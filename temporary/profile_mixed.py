import cProfile
import pstats
from pathlib import Path

from puzzles.thermo_killer_001 import create_puzzle as mixed_001
from puzzles.thermo_killer_002 import create_puzzle as mixed_002


def profile_puzzle(name, factory):
    print(f"\n{'=' * 60}")
    print(f"PROFILING: {name}")
    print("=" * 60)

    puzzle = factory()

    profiler = cProfile.Profile()
    profiler.enable()

    status, solutions, solver = puzzle.check_uniqueness()

    profiler.disable()

    print(f"\nStatus: {status}")
    print(f"Solutions: {len(solutions)}")
    print(f"Search decisions: {solver.nodes}")
    print(f"Backtracks: {solver.backtracks}")
    print(f"Propagation rounds: {solver.propagation_rounds}")

    print("\nTOP 25 FUNCTIONS BY CUMULATIVE TIME")
    print("-" * 60)

    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats(25)

    Path("output").mkdir(exist_ok=True)

    filename = f"output/profile_{name}.prof"
    stats.dump_stats(filename)

    print(f"\nProfile saved to {filename}")


if __name__ == "__main__":
    profile_puzzle("mixed_001", mixed_001)
    profile_puzzle("mixed_002", mixed_002)