
import json
import random
from pathlib import Path

# ==========================================
# EXPERIMENT SETTINGS
# ==========================================

GIVEN_COUNTS = [20, 25, 30]
PATTERNS_PER_GRID = 5
RANDOM_SEED = 2026

INPUT_DIR = Path("puzzles/controlled")
OUTPUT_FILE = INPUT_DIR / "givens_experiment.json"

GRID_FILES = [
    "standard_grids.json",
    "standard_diagonal_grids.json",
    "standard_anti_knight_grids.json",
    "standard_anti_king_grids.json",
]


def generate_experiment():
    rng = random.Random(RANDOM_SEED)
    experiments = []

    for filename in GRID_FILES:
        path = INPUT_DIR / filename

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        rules = data["rules"]
        group = Path(filename).stem.removesuffix("_grids")

        for grid_index, solution in enumerate(data["grids"], start=1):
            for pattern_index in range(1, PATTERNS_PER_GRID + 1):
                # Same shuffled cell order for all given counts.
                positions = list(range(81))
                rng.shuffle(positions)

                for given_count in GIVEN_COUNTS:
                    selected = set(positions[:given_count])

                    puzzle = [
                        [
                            solution[r][c] if r * 9 + c in selected else 0
                            for c in range(9)
                        ]
                        for r in range(9)
                    ]

                    experiments.append({
                        "id": (
                            f"{group}_g{grid_index:02d}"
                            f"_p{pattern_index:02d}"
                            f"_n{given_count:02d}"
                        ),
                        "group": group,
                        "grid_index": grid_index,
                        "pattern_index": pattern_index,
                        "given_count": given_count,
                        "reference_rules": rules,
                        "solve_rules": {
                            "standard": True,
                            "diagonal": False,
                            "anti_knight": False,
                            "anti_king": False,
                        },
                        "puzzle": puzzle,
                        "solution": solution,
                    })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "settings": {
                    "given_counts": GIVEN_COUNTS,
                    "patterns_per_grid": PATTERNS_PER_GRID,
                    "random_seed": RANDOM_SEED,
                },
                "experiments": experiments,
            },
            f,
            indent=2,
        )

    print(f"Generated {len(experiments)} puzzles.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_experiment()