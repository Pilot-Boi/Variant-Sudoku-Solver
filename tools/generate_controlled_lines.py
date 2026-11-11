
"""Generate six controlled variant-Sudoku datasets.

Run from project root:
    python -m tools.generate_controlled_lines
"""

import json
import random
from pathlib import Path

from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution

SOURCE = Path("puzzles/controlled/givens_experiment.json")
OUTPUT_DIR = Path("puzzles/controlled")

VARIANTS = (
    "arrow",
    "between_line",
    "german_whisper",
    "palindrome",
    "renban",
    "little_killer",
)

COUNTS = (2, 4, 6)
SEED = 2026
MAX_PATH_TRIALS = 5000
SELECTION_TRIALS = 150


def digit(solution, cell):
    return solution[cell[0]][cell[1]]


def neighbors(cell):
    r, c = cell
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < 9 and 0 <= nc < 9:
                yield nr, nc


def all_cells():
    return [(r, c) for r in range(9) for c in range(9)]


def random_path(rng, length):
    path = [rng.choice(all_cells())]

    while len(path) < length:
        options = [
            cell for cell in neighbors(path[-1])
            if cell not in path
        ]

        if not options:
            return None

        path.append(rng.choice(options))

    return tuple(path)


def canonical_path(path):
    forward = tuple(path)
    backward = tuple(reversed(path))
    return min(forward, backward)


def valid_line(variant, solution, path):
    values = [digit(solution, cell) for cell in path]

    if variant == "german_whisper":
        return all(
            abs(a - b) >= 5
            for a, b in zip(values, values[1:])
        )

    if variant == "renban":
        return (
            len(set(values)) == len(values)
            and max(values) - min(values) == len(values) - 1
        )

    if variant == "between_line":
        low = min(values[0], values[-1])
        high = max(values[0], values[-1])
        return all(low < v < high for v in values[1:-1])

    if variant == "palindrome":
        return values == values[::-1]

    raise ValueError(variant)


def generate_line_candidates(variant, solution, rng):
    candidates = {}
    lengths = {
        "german_whisper": (3, 4, 5),
        "renban": (3, 4),
        "between_line": (3, 4, 5),
    }[variant]

    for _ in range(MAX_PATH_TRIALS):
        path = random_path(rng, rng.choice(lengths))

        if path is None or not valid_line(variant, solution, path):
            continue

        path = canonical_path(path)
        candidates[path] = {
            "cells": [list(cell) for cell in path]
        }

    return list(candidates.values())


def generate_palindrome_candidates(solution):
    """Construct valid 3-cell palindromes directly.

    A-B-A requires equal endpoint digits. The endpoints
    must be different cells; Standard Sudoku rules will
    reject equal digits in the same row, column, or box.
    """
    candidates = {}

    for middle in all_cells():
        adjacent = list(neighbors(middle))

        for i, a in enumerate(adjacent):
            for b in adjacent[i + 1:]:
                if digit(solution, a) != digit(solution, b):
                    continue

                path = canonical_path((a, middle, b))
                candidates[path] = {
                    "cells": [list(cell) for cell in path]
                }

    return list(candidates.values())


def generate_arrow_candidates(solution, rng):
    candidates = {}

    for _ in range(MAX_PATH_TRIALS):
        # Single-cell circle and 2- or 3-cell shaft.
        path = random_path(rng, rng.choice((3, 4)))

        if path is None:
            continue

        circle = path[0]
        shaft = path[1:]

        if digit(solution, circle) != sum(
            digit(solution, cell) for cell in shaft
        ):
            continue

        key = (circle, shaft)

        candidates[key] = {
            "circle_cells": [list(circle)],
            "arrow_cells": [list(cell) for cell in shaft],
        }

    return list(candidates.values())


def generate_little_killer_candidates(solution):
    """All diagonals of length >= 3, in both orientations."""
    candidates = []

    for direction in ("down-right", "down-left"):
        dr, dc = (1, 1) if direction == "down-right" else (1, -1)

        starts = (
            [(0, c) for c in range(9)]
            + (
                [(r, 0) for r in range(1, 9)]
                if dc == 1
                else [(r, 8) for r in range(1, 9)]
            )
        )

        for start in starts:
            path = []
            r, c = start

            while 0 <= r < 9 and 0 <= c < 9:
                path.append((r, c))
                r += dr
                c += dc

            if len(path) < 3:
                continue

            candidates.append({
                "cells": [list(cell) for cell in path],
                "sum": sum(digit(solution, cell) for cell in path),
                "direction": direction,
            })

    return candidates


def clue_cells(clue):
    if "circle_cells" in clue:
        return {
            tuple(cell)
            for cell in clue["circle_cells"] + clue["arrow_cells"]
        }

    return {tuple(cell) for cell in clue["cells"]}


def select_clues(candidates, rng, variant):
    """Prefer six non-overlapping clues.

    Palindrome and Little Killer may require overlapping
    clue cells because of their geometric restrictions.
    Distinct clues are still required.
    """
    if len(candidates) < max(COUNTS):
        raise RuntimeError(
            f"{variant}: only {len(candidates)} valid clues available"
        )

    for _ in range(SELECTION_TRIALS):
        shuffled = list(candidates)
        rng.shuffle(shuffled)

        chosen = []
        occupied = set()

        for clue in shuffled:
            cells = clue_cells(clue)

            if occupied.isdisjoint(cells):
                chosen.append(clue)
                occupied.update(cells)

            if len(chosen) == max(COUNTS):
                return chosen, False

    if variant not in ("palindrome", "little_killer"):
        raise RuntimeError(
            f"{variant}: cannot select six non-overlapping clues"
        )

    # For geometry-limited variants, minimize overlap
    # rather than weakening or inventing clues.
    remaining = list(candidates)
    chosen = []
    occupied = set()

    while len(chosen) < max(COUNTS):
        rng.shuffle(remaining)
        remaining.sort(
            key=lambda clue: len(clue_cells(clue) & occupied)
        )

        clue = remaining.pop(0)
        chosen.append(clue)
        occupied.update(clue_cells(clue))

    return chosen, True


def generate_clues(variant, solution, rng):
    if variant == "arrow":
        candidates = generate_arrow_candidates(solution, rng)

    elif variant == "palindrome":
        candidates = generate_palindrome_candidates(solution)

    elif variant == "little_killer":
        candidates = generate_little_killer_candidates(solution)

    else:
        candidates = generate_line_candidates(variant, solution, rng)

    return select_clues(candidates, rng, variant)


def apply_clue(puzzle, variant, clue):
    if variant == "arrow":
        puzzle.add_arrow(
            [tuple(cell) for cell in clue["circle_cells"]],
            [tuple(cell) for cell in clue["arrow_cells"]],
        )

    elif variant == "between_line":
        puzzle.add_between_line(
            [tuple(cell) for cell in clue["cells"]]
        )

    elif variant == "german_whisper":
        puzzle.add_german_whispers(
            [tuple(cell) for cell in clue["cells"]]
        )

    elif variant == "palindrome":
        puzzle.add_palindrome(
            [tuple(cell) for cell in clue["cells"]]
        )

    elif variant == "renban":
        puzzle.add_renban(
            [tuple(cell) for cell in clue["cells"]]
        )

    elif variant == "little_killer":
        puzzle.add_little_killer(
            [tuple(cell) for cell in clue["cells"]],
            clue["sum"],
        )

    else:
        raise ValueError(variant)


def reference_assignment(solution):
    return {
        (r, c): solution[r][c]
        for r in range(9)
        for c in range(9)
    }


def validate_clues(base, variant, clues):
    puzzle = SudokuPuzzle(base["puzzle"])

    for clue in clues:
        apply_clue(puzzle, variant, clue)

    errors = validate_solution(
        puzzle,
        reference_assignment(base["solution"]),
    )

    # validate_solution returns a LIST of errors.
    # An empty list means success.
    if errors:
        raise ValueError(
            f"{base['id']} / {variant}: {errors}"
        )


def main():
    with SOURCE.open(encoding="utf-8") as file:
        source = json.load(file)["experiments"]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for variant_index, variant in enumerate(VARIANTS):
        rng = random.Random(SEED + 100 + variant_index)
        shared = {}
        records = []
        overlapping_sets = 0

        for base in source:
            key = (
                base["group"],
                base["grid_index"],
                base["pattern_index"],
            )

            if key not in shared:
                clues, overlaps = generate_clues(
                    variant, base["solution"], rng
                )

                shared[key] = {
                    "solution": base["solution"],
                    "clues": clues,
                    "overlaps": overlaps,
                }

                if overlaps:
                    overlapping_sets += 1

            saved = shared[key]

            if saved["solution"] != base["solution"]:
                raise ValueError(
                    f"Reference grid mismatch: {base['id']}"
                )

            for count in COUNTS:
                selected = saved["clues"][:count]
                validate_clues(base, variant, selected)

                record = dict(base)
                record.update({
                    "id": f"{base['id']}_{variant}_{count:02d}",
                    "base_id": base["id"],
                    "variant": variant,
                    "clue_count": count,
                    "clues": selected,
                    "clues_overlap": saved["overlaps"],
                })

                records.append(record)

        output = OUTPUT_DIR / f"{variant}_experiment.json"

        with output.open("w", encoding="utf-8") as file:
            json.dump({
                "settings": {
                    "variant": variant,
                    "clue_counts": list(COUNTS),
                    "random_seed": SEED + 100 + variant_index,
                    "nested_clues": True,
                    "shared_across_givens": True,
                    "overlapping_clue_sets": overlapping_sets,
                },
                "experiments": records,
            }, file, indent=2)

        print(
            f"{variant}: {len(records)} configurations, "
            f"{len(shared)} shared clue sets, "
            f"{overlapping_sets} overlapping sets"
        )
        print(f"  Saved to {output}")

    print("\nAll six Batch 2 datasets generated and validated!")


if __name__ == "__main__":
    main()