
"""
Puzzle: Thermometer Sudoku #001
Source: https://sudokupad.app/gjvgfg1ovq

Rules:
- Standard Sudoku rules apply.
- Digits strictly increase from bulb to tip
  along each thermometer.
- No given digits.

Benchmark (initial CSP implementation):
- First solution: 0.335088 seconds
- Uniqueness check: 1.219904 seconds
- Unique solution confirmed.
"""

from sudoku.puzzle import SudokuPuzzle


NAME = "Thermometer Sudoku #001"
SOURCE = "https://sudokupad.app/gjvgfg1ovq"

GRID = [[0] * 9 for _ in range(9)]

THERMOMETERS = [
    [(3, 0), (2, 0), (1, 0), (0, 1)],
    [(2, 1), (2, 2)],
    [(1, 3), (2, 3), (3, 3), (3, 4),
     (4, 4), (4, 5), (5, 6)],
    [(1, 4), (2, 4), (2, 5), (3, 5),
     (3, 6)],
    [(0, 5), (0, 6), (0, 7), (1, 8),
     (2, 7)],
    [(4, 8), (5, 7)],
    [(6, 3), (6, 2), (5, 2), (5, 1)],
    [(7, 0), (8, 1)],
    [(7, 4), (6, 4)],
    [(8, 5), (8, 6), (7, 7),
     (6, 8), (5, 8)]
]


def create_puzzle():
    """Create a fresh instance of this puzzle."""
    puzzle = SudokuPuzzle(GRID)

    for cells in THERMOMETERS:
        puzzle.add_thermometer(cells)

    return puzzle
