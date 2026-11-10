"""
Seesaw by Celery

Imported from https://sudokupad.app/x2k2gvzqw4

Rules:
Normal sudoku rules apply. 

Digits in a cage sum to the total in the top left corner (if given). Digits cannot repeat within a cage.
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Seesaw — Celery"
SOURCE_URL = "https://sudokupad.app/x2k2gvzqw4"

# Solution string provided by the source puzzle data.
SOLUTION = "872153946693784521514629387326415798951378462748962153469837215135246879287591634"


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
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 7), (1, 8)], 13)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0), (7, 1)], 14)
    puzzle.add_killer_cage([(6, 4), (7, 3), (7, 4)], 9)
    puzzle.add_killer_cage([(7, 6), (8, 6)], 14)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 8), (6, 7), (6, 8)], 17)
    puzzle.add_killer_cage([(5, 6), (5, 7), (6, 5), (6, 6), (7, 5)], 21)
    puzzle.add_killer_cage([(2, 5), (3, 5), (3, 6)], 21)
    puzzle.add_killer_cage([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2)], 18)
    puzzle.add_killer_cage([(4, 1), (4, 2), (4, 3), (5, 1)], 13)
    puzzle.add_killer_cage([(1, 4), (1, 5), (2, 4)], 14)
    puzzle.add_sumless_killer_cage([(2, 8), (3, 7), (3, 8)])

    return puzzle
