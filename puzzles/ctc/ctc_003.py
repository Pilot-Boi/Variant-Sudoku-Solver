"""
Mut zur Lücke! by Wuschel

Imported from https://sudokupad.app/q9tbRnF4Nh

Rules:
Normal sudoku rules apply. Digits on the indicated diagonal may not repeat. Digits in cages may not repeat and sum to the indicated total. The inequality sign ‘points' towards the smaller digit.
"""

from sudoku.puzzle import SudokuPuzzle
from sudoku.constraints import AllDifferentConstraint

NAME = "Mut zur Lücke! — Wuschel"
SOURCE_URL = "https://sudokupad.app/q9tbRnF4Nh"

# Solution string provided by the source puzzle data.
SOLUTION = "467953812183267495529418637874591263632874159951326748296185374318749526745632981"


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_inequality((1, 0), (0, 0), "<")
    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0), (2, 1)], 12)
    puzzle.add_killer_cage([(4, 2), (4, 1), (4, 0), (5, 0)], 20)
    puzzle.add_killer_cage([(6, 1), (6, 2), (7, 2), (8, 2)], 28)
    puzzle.add_killer_cage([(5, 5), (6, 5), (7, 5), (6, 4)], 28)
    puzzle.add_killer_cage([(1, 3), (2, 3), (3, 3), (2, 4)], 12)
    puzzle.add_killer_cage([(0, 4), (0, 5), (0, 6), (1, 6)], 20)
    puzzle.add_killer_cage([(2, 7), (2, 6), (3, 6), (4, 6)], 12)
    puzzle.add_killer_cage([(5, 8), (6, 8), (4, 8), (6, 7)], 28)

    # Main diagonal only.
    puzzle.add_constraint(
        AllDifferentConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
            required_values=set(range(1, 10)),
        )
    )

    return puzzle
