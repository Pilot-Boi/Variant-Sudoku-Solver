
import json
from pathlib import Path

from ortools.sat.python import cp_model

# ==========================================
# GENERATOR SETTINGS
# ==========================================

GRID_COUNT = 5

USE_STANDARD = True
USE_DIAGONAL = False
USE_ANTI_KNIGHT = False
USE_ANTI_KING = True

# ==========================================
# OUTPUT SETTINGS
# ==========================================

enabled_rules = []

if USE_STANDARD:
    enabled_rules.append("standard")

if USE_DIAGONAL:
    enabled_rules.append("diagonal")

if USE_ANTI_KNIGHT:
    enabled_rules.append("anti_knight")

if USE_ANTI_KING:
    enabled_rules.append("anti_king")

OUTPUT = Path(
    "puzzles/controlled/"
    + "_".join(enabled_rules)
    + "_grids.json"
)

def normalize_grid(grid):
    """Replace digits by their order of first appearance."""
    mapping = {}
    next_digit = 1
    normalized = []

    for row in grid:
        normalized_row = []

        for digit in row:
            if digit not in mapping:
                mapping[digit] = next_digit
                next_digit += 1

            normalized_row.append(mapping[digit])

        normalized.append(normalized_row)

    return normalized

def generate_grid(seed, previous_grids):
    model = cp_model.CpModel()

    cells = [
        [
            model.NewIntVar(1, 9, f"r{r}c{c}")
            for c in range(9)
        ]
        for r in range(9)
    ]

    # Symmetry breaking: fix the first row.
    # Every valid grid can be relabeled to satisfy this.
    for c in range(9):
        model.Add(cells[0][c] == c + 1)
    
    # ==========================================
    # STANDARD SUDOKU
    # ==========================================

    if USE_STANDARD:
        # Rows
        for r in range(9):
            model.AddAllDifferent(cells[r])

        # Columns
        for c in range(9):
            model.AddAllDifferent(
                [cells[r][c] for r in range(9)]
            )

        # 3x3 boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                model.AddAllDifferent([
                    cells[r][c]
                    for r in range(br, br + 3)
                    for c in range(bc, bc + 3)
                ])

    # ==========================================
    # DIAGONAL SUDOKU
    # ==========================================

    if USE_DIAGONAL:
        model.AddAllDifferent(
            [cells[i][i] for i in range(9)]
        )

        model.AddAllDifferent(
            [cells[i][8 - i] for i in range(9)]
        )

    # ==========================================
    # ANTI-KNIGHT
    # ==========================================

    if USE_ANTI_KNIGHT:
        knight_moves = [
            (1, 2), (1, -2),
            (2, 1), (2, -1),
        ]

        for r in range(9):
            for c in range(9):
                for dr, dc in knight_moves:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < 9 and 0 <= nc < 9:
                        model.Add(
                            cells[r][c] != cells[nr][nc]
                        )

    # ==========================================
    # ANTI-KING
    # ==========================================

    if USE_ANTI_KING:
        king_moves = [
            (1, 1), (1, -1),
        ]

        for r in range(9):
            for c in range(9):
                for dr, dc in king_moves:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < 9 and 0 <= nc < 9:
                        model.Add(
                            cells[r][c] != cells[nr][nc]
                        )

    # ==========================================
    # ONE VARIANT ENABLED
    # ==========================================
    
    if not USE_STANDARD:
        raise ValueError(
            "Standard Sudoku must always be enabled."
        )

    variant_count = sum([
        USE_DIAGONAL,
        USE_ANTI_KNIGHT,
        USE_ANTI_KING,
    ])

    if variant_count > 1:
        raise ValueError(
            "Enable at most one additional variant rule."
        )
        
    # ==========================================
    # EXCLUDE PREVIOUS GRIDS
    # ==========================================

    for previous_index, previous in enumerate(previous_grids):
        matches = []

        for r in range(9):
            for c in range(9):
                match = model.NewBoolVar(
                    f"previous_{previous_index}_{r}_{c}"
                )

                model.Add(
                    cells[r][c] == previous[r][c]
                ).OnlyEnforceIf(match)

                model.Add(
                    cells[r][c] != previous[r][c]
                ).OnlyEnforceIf(match.Not())

                matches.append(match)

        # At least one cell must differ.
        model.Add(sum(matches) <= 80)

    # ==========================================
    # SOLVE
    # ==========================================

    solver = cp_model.CpSolver()

    solver.parameters.random_seed = seed
    solver.parameters.num_search_workers = 1
    solver.parameters.max_time_in_seconds = 120

    status = solver.Solve(model)

    if status not in (
        cp_model.OPTIMAL,
        cp_model.FEASIBLE,
    ):
        raise RuntimeError(
            "Could not generate grid "
            f"(status: {solver.StatusName(status)})"
        )

    return [
        [
            solver.Value(cells[r][c])
            for c in range(9)
        ]
        for r in range(9)
    ]

def main():
    grids = []

    print("Enabled constraints:", ", ".join(enabled_rules))
    print(f"Requested grids: {GRID_COUNT}")
    print()

    for index in range(GRID_COUNT):
        print(f"Generating grid {index + 1}/{GRID_COUNT}...")

        try:
            grid = generate_grid(
                seed=2026 + index,
                previous_grids=grids,
            )
        except RuntimeError as exc:
            if "INFEASIBLE" in str(exc):
                print(
                    "\nNo additional distinct grids exist "
                    "for this constraint combination."
                )
                break

            raise

        normalized = normalize_grid(grid)

        if any(normalize_grid(old) == normalized for old in grids):
            raise RuntimeError(
                "Duplicate grid detected after digit normalization."
            )

        grids.append(grid)

        for row in grid:
            print(" ".join(map(str, row)))

        print()

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT.write_text(
        json.dumps(
            {
                "rules": {
                    "standard": USE_STANDARD,
                    "diagonal": USE_DIAGONAL,
                    "anti_knight": USE_ANTI_KNIGHT,
                    "anti_king": USE_ANTI_KING,
                },
                "grids": grids,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Saved {len(grids)} grids to {OUTPUT}")


if __name__ == "__main__":
    main()
