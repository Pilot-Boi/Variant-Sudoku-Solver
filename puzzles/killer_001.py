
"""
Killer Sudoku #001

Source: https://sudokupad.app/ofnww6z458

Rules:
- Standard 9x9 Sudoku.
- Digits in each cage sum to its target.
- Digits cannot repeat within a cage.
- Some cells are not part of a cage.

Coordinates are zero-indexed (row, column).
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Killer Sudoku #001"
SOURCE = "https://sudokupad.app/ofnww6z458"

GRID = [[0] * 9 for _ in range(9)]

# Each entry is (target_sum, cells).
CAGES = [
    (15, [(0, 0), (0, 1), (1, 0)]),
    (24, [(0, 2), (1, 2), (1, 3)]),
    (22, [(0, 6), (1, 5), (1, 6)]),
    (11, [(0, 7), (0, 8), (1, 8)]),

    (19, [(2, 0), (2, 1), (3, 1)]),
    (15, [(2, 2), (2, 3), (3, 2), (4, 2)]),
    (17, [(2, 4), (2, 5), (2, 6), (3, 6)]),
    (21, [(2, 7), (2, 8), (3, 7)]),

    (16, [(3, 0), (4, 0), (5, 0)]),
    (32, [(3, 4), (4, 3), (4, 4), (4, 5),
          (5, 4)]),

    (18, [(4, 6), (5, 6), (6, 5),(6, 6)]),
    (8, [(4, 7), (4, 8)]),

    (20, [(5, 1), (6, 0), (6, 1)]),
    (20, [(5, 2), (6, 2), (6, 3), (6, 4)]),
    (22, [(5, 7), (6, 7), (6, 8)]),

    (12, [(7, 0), (8, 0), (8, 1)]),
    (23, [(7, 2), (7, 3), (8, 2)]),
    (20, [(7, 5), (7, 6), (8, 6)]),
    (12, [(7, 8), (8, 7), (8, 8)]),
    (8, [(8, 4), (8, 5)])
]


def create_puzzle():
    puzzle = SudokuPuzzle(GRID)

    for target_sum, cells in CAGES:
        puzzle.add_killer_cage(cells, target_sum)

    return puzzle
