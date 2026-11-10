"""
Layla by Philip Newman

Imported from https://sudokupad.app/mJqT6RDG2L

Rules:
Normal sudoku rules apply. Digits in cages cannot repeat and must sum to the total given.
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Layla — Philip Newman"
SOURCE_URL = "https://sudokupad.app/mJqT6RDG2L"

# Solution string provided by the source puzzle data.
SOLUTION = "914325876725468193368791425591283764486157239237649518152836947649572381873914652"


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
    puzzle.add_killer_cage([(1, 6), (2, 6), (2, 7)], 7)
    puzzle.add_killer_cage([(4, 8), (5, 8), (6, 8)], 24)
    puzzle.add_killer_cage([(2, 5), (3, 5), (3, 6), (4, 6)], 13)
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0)], 37)
    puzzle.add_killer_cage([(7, 5), (7, 6), (8, 4), (8, 5), (8, 6)], 16)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 1), (6, 2), (6, 3), (7, 2)], 37)

    return puzzle
