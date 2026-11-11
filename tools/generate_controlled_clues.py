
"""Generate controlled experiments for five Sudoku variants.

Run from the repository root:
    python -m tools.generate_controlled_clues
"""

import json
import random
from pathlib import Path

from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution

INPUT_FILE = Path("puzzles/controlled/givens_experiment.json")
OUTPUT_DIR = Path("puzzles/controlled")

VARIANTS = ("killer", "kropki", "xv", "inequality", "parity")
COUNTS = (2, 4, 6)
SEED = 2026
MAX_ATTEMPTS = 300

# All coordinates are zero-indexed.
def orthogonal_neighbors(cell):
    r, c = cell
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 9 and 0 <= nc < 9:
            yield (nr, nc)


def orthogonal_pairs():
    for r in range(9):
        for c in range(9):
            if r < 8:
                yield ((r, c), (r + 1, c))
            if c < 8:
                yield ((r, c), (r, c + 1))


def value(solution, cell):
    return solution[cell[0]][cell[1]]


def choose_disjoint(candidates, rng, count=6):
    """Choose clues with no shared cells."""
    candidates = list(candidates)
    rng.shuffle(candidates)

    selected = []
    occupied = set()

    for clue, cells in candidates:
        if occupied.isdisjoint(cells):
            selected.append(clue)
            occupied.update(cells)

            if len(selected) == count:
                return selected

    return None


def generate_killer(solution, rng):
    """Connected cages of 2-4 distinct digits."""
    for _ in range(MAX_ATTEMPTS):
        occupied = set()
        cages = []

        for _ in range(max(COUNTS)):
            starts = [
                (r, c)
                for r in range(9)
                for c in range(9)
                if (r, c) not in occupied
            ]
            rng.shuffle(starts)

            chosen = None

            for start in starts:
                size = rng.choice((2, 3, 4))
                cells = [start]
                used_digits = {value(solution, start)}

                while len(cells) < size:
                    frontier = {
                        neighbor
                        for cell in cells
                        for neighbor in orthogonal_neighbors(cell)
                        if neighbor not in occupied
                        and neighbor not in cells
                        and value(solution, neighbor) not in used_digits
                    }

                    if not frontier:
                        break

                    next_cell = rng.choice(sorted(frontier))
                    cells.append(next_cell)
                    used_digits.add(value(solution, next_cell))

                if len(cells) == size:
                    chosen = cells
                    break

            if chosen is None:
                break

            occupied.update(chosen)
            cages.append({
                "cells": [list(cell) for cell in chosen],
                "sum": sum(value(solution, cell) for cell in chosen),
            })

        if len(cages) == max(COUNTS):
            return cages

    raise RuntimeError("Could not generate six Killer cages")


def generate_kropki(solution, rng):
    candidates = []

    for a, b in orthogonal_pairs():
        x, y = value(solution, a), value(solution, b)

        if abs(x - y) == 1:
            dot_type = "white"
        elif max(x, y) == 2 * min(x, y):
            dot_type = "black"
        else:
            continue

        candidates.append((
            {
                "cells": [list(a), list(b)],
                "type": dot_type,
            },
            (a, b),
        ))

    return choose_disjoint(candidates, rng)


def generate_xv(solution, rng):
    candidates = []

    for a, b in orthogonal_pairs():
        total = value(solution, a) + value(solution, b)

        if total not in (5, 10):
            continue

        candidates.append((
            {
                "cells": [list(a), list(b)],
                "marker": "V" if total == 5 else "X",
            },
            (a, b),
        ))

    return choose_disjoint(candidates, rng)


def generate_inequality(solution, rng):
    candidates = []

    for a, b in orthogonal_pairs():
        candidates.append((
            {
                "cells": [list(a), list(b)],
                "operator": "<" if value(solution, a) < value(solution, b) else ">",
            },
            (a, b),
        ))

    return choose_disjoint(candidates, rng)


def generate_parity(solution, rng):
    candidates = []

    for r in range(9):
        for c in range(9):
            cell = (r, c)
            candidates.append((
                {
                    "cell": [r, c],
                    "parity": "odd" if value(solution, cell) % 2 else "even",
                },
                (cell,),
            ))

    return choose_disjoint(candidates, rng)


GENERATORS = {
    "killer": generate_killer,
    "kropki": generate_kropki,
    "xv": generate_xv,
    "inequality": generate_inequality,
    "parity": generate_parity,
}


def apply_clue(puzzle, variant, clue):
    if variant == "killer":
        puzzle.add_killer_cage(
            [tuple(cell) for cell in clue["cells"]],
            clue["sum"],
        )

    elif variant == "kropki":
        a, b = map(tuple, clue["cells"])
        puzzle.add_kropki_dot(a, b, clue["type"])

    elif variant == "xv":
        a, b = map(tuple, clue["cells"])
        puzzle.add_xv(a, b, clue["marker"])

    elif variant == "inequality":
        a, b = map(tuple, clue["cells"])
        puzzle.add_inequality(a, b, clue["operator"])

    elif variant == "parity":
        cell = tuple(clue["cell"])
        if clue["parity"] == "odd":
            puzzle.add_odd_cell(cell)
        else:
            puzzle.add_even_cell(cell)

    else:
        raise ValueError(f"Unknown variant: {variant}")


def reference_assignment(solution):
    return {
        (r, c): solution[r][c]
        for r in range(9)
        for c in range(9)
    }

def validate_clues(base, variant, clues):
    assignment = reference_assignment(base["solution"])

    # Verify the reference solution satisfies Standard Sudoku.
    baseline = SudokuPuzzle(base["puzzle"])

    errors = validate_solution(baseline, assignment)

    if errors:
        raise ValueError(
            f"Baseline reference solution invalid "
            f"for {base['id']}:\n{errors}"
        )

    # Verify each generated clue individually.
    for index, clue in enumerate(clues, start=1):
        puzzle = SudokuPuzzle(base["puzzle"])
        apply_clue(puzzle, variant, clue)

        errors = validate_solution(puzzle, assignment)

        if errors:
            raise ValueError(
                f"Invalid {variant} clue #{index} "
                f"for {base['id']}:\n"
                f"Clue: {clue}\n"
                f"Errors: {errors}"
            )

    # Verify all clues together.
    puzzle = SudokuPuzzle(base["puzzle"])

    for clue in clues:
        apply_clue(puzzle, variant, clue)

    errors = validate_solution(puzzle, assignment)

    if errors:
        raise ValueError(
            f"Combined {variant} clues invalid "
            f"for {base['id']}:\n"
            f"Errors: {errors}"
        )

def main():
    with INPUT_FILE.open(encoding="utf-8") as f:
        source = json.load(f)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for variant_index, variant in enumerate(VARIANTS):
        rng = random.Random(SEED + variant_index)
        shared_clues = {}
        records = []

        for base in source["experiments"]:
            key = (
                base["group"],
                base["grid_index"],
                base["pattern_index"],
            )

            if key not in shared_clues:
                clues = GENERATORS[variant](base["solution"], rng)

                if clues is None or len(clues) != max(COUNTS):
                    raise RuntimeError(
                        f"Not enough {variant} clues for {base['id']}"
                    )

                shared_clues[key] = {
                    "solution": base["solution"],
                    "clues": clues,
                }

            saved = shared_clues[key]

            if saved["solution"] != base["solution"]:
                raise ValueError(
                    f"Reference grid mismatch: {base['id']}"
                )

            clues = saved["clues"]

            for count in COUNTS:
                selected = clues[:count]

                validate_clues(base, variant, selected)

                record = dict(base)
                record["id"] = (
                    f"{base['id']}_{variant}_{count:02d}"
                )
                record["base_id"] = base["id"]
                record["variant"] = variant
                record["clue_count"] = count
                record["clues"] = selected

                records.append(record)

        output_file = OUTPUT_DIR / f"{variant}_experiment.json"

        with output_file.open("w", encoding="utf-8") as f:
            json.dump(
                {
                    "settings": {
                        "variant": variant,
                        "clue_counts": list(COUNTS),
                        "random_seed": SEED + variant_index,
                        "nested_clues": True,
                        "shared_across_givens": True,
                        "non_overlapping": True,
                        "negative_constraints": False,
                    },
                    "experiments": records,
                },
                f,
                indent=2,
            )

        print(
            f"{variant}: {len(records)} configurations, "
            f"{len(shared_clues)} shared clue sets"
        )
        print(f"  Saved to {output_file}")

    print("\nAll five datasets generated and validated!")


if __name__ == "__main__":
    main()