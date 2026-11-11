"""Generate nested, solution-consistent thermometer clues for controlled Sudoku puzzles.

Run from the repository root:
    python -m tools.generate_thermometer_experiment
"""

import json
import random
from pathlib import Path

INPUT_FILE = Path('puzzles/controlled/givens_experiment.json')
OUTPUT_FILE = Path('puzzles/controlled/thermometer_experiment.json')
THERMOMETER_COUNTS = (2, 4, 6)
MIN_LENGTH = 2
MAX_LENGTH = 5
RANDOM_SEED = 2026
MAX_ATTEMPTS = 100


def neighbors(cell):
    r, c = cell
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 9 and 0 <= nc < 9:
            yield (nr, nc)


def all_increasing_paths(solution):
    """Return all orthogonally connected, strictly increasing paths of allowed lengths."""
    paths = []

    def extend(path):
        if len(path) >= MIN_LENGTH:
            paths.append(tuple(path))
        if len(path) == MAX_LENGTH:
            return
        for next_cell in neighbors(path[-1]):
            if next_cell in path:
                continue
            r, c = path[-1]
            nr, nc = next_cell
            if solution[nr][nc] > solution[r][c]:
                extend(path + [next_cell])

    for r in range(9):
        for c in range(9):
            extend([(r, c)])
    return paths


def choose_thermometers(solution, rng):
    candidates = all_increasing_paths(solution)
    rng.shuffle(candidates)
    chosen = []
    occupied = set()
    for path in candidates:
        if occupied.isdisjoint(path):
            chosen.append(path)
            occupied.update(path)
            if len(chosen) == max(THERMOMETER_COUNTS):
                return chosen
    return None



def main():
    with INPUT_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    rng = random.Random(RANDOM_SEED)
    records = []

    # One set of thermometer paths per reference grid + givens pattern.
    # The 20-, 25-, and 30-given versions share these paths.
    thermometer_sets = {}

    for experiment in data["experiments"]:
        key = (
            experiment["group"],
            experiment["grid_index"],
            experiment["pattern_index"],
        )

        solution = experiment["solution"]

        if key not in thermometer_sets:
            selected = None

            for _ in range(MAX_ATTEMPTS):
                selected = choose_thermometers(solution, rng)
                if selected is not None:
                    break

            if selected is None:
                raise RuntimeError(
                    f"Could not place six thermometers: {experiment['id']}"
                )

            thermometer_sets[key] = {
                "solution": solution,
                "paths": selected,
            }

        saved = thermometer_sets[key]

        # All three givens counts must use the same reference solution.
        if saved["solution"] != solution:
            raise ValueError(
                f"Reference solution mismatch for {experiment['id']}"
            )

        selected = saved["paths"]

        for count in THERMOMETER_COUNTS:
            record = dict(experiment)
            record["id"] = f"{experiment['id']}_t{count:02d}"
            record["base_id"] = experiment["id"]
            record["thermometer_count"] = count
            record["thermometers"] = [
                [[r, c] for r, c in path]
                for path in selected[:count]
            ]
            records.append(record)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "settings": {
                    "thermometer_counts": list(THERMOMETER_COUNTS),
                    "min_length": MIN_LENGTH,
                    "max_length": MAX_LENGTH,
                    "random_seed": RANDOM_SEED,
                    "non_overlapping": True,
                    "orthogonal_paths": True,
                    "nested_clues": True,
                    "shared_across_givens": True,
                },
                "experiments": records,
            },
            f,
            indent=2,
        )

    print(f"Generated {len(records)} configurations.")
    print(f"Shared thermometer sets: {len(thermometer_sets)}")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
