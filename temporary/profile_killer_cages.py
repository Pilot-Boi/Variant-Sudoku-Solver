import time
from collections import defaultdict

from puzzles.thermo_killer_001 import create_puzzle as mixed_001
from puzzles.thermo_killer_002 import create_puzzle as mixed_002
from sudoku.constraints import KillerCageConstraint


def profile_cages(name, factory):
    puzzle = factory()

    results = defaultdict(
        lambda: {"calls": 0, "seconds": 0.0}
    )

    original = KillerCageConstraint._find_supports

    def timed_find_supports(self, domains):
        start = time.perf_counter()

        try:
            return original(self, domains)
        finally:
            elapsed = time.perf_counter() - start

            key = (
                len(self.variables),
                self.target_sum,
                tuple(self.variables),
            )

            results[key]["calls"] += 1
            results[key]["seconds"] += elapsed

    KillerCageConstraint._find_supports = timed_find_supports

    try:
        status, solutions, solver = puzzle.check_uniqueness()
    finally:
        KillerCageConstraint._find_supports = original

    print(f"\n{name}: {status}")
    print("-" * 75)

    for (size, target, cells), data in sorted(
        results.items(),
        key=lambda item: item[1]["seconds"],
        reverse=True,
    ):
        print(
            f"{size} cells | "
            f"sum {target:2d} | "
            f"{data['calls']:4d} calls | "
            f"{data['seconds']:.4f}s | "
            f"{cells}"
        )


if __name__ == "__main__":
    profile_cages("Mixed #001", mixed_001)
    profile_cages("Mixed #002", mixed_002)