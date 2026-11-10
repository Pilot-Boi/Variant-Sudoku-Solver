
from sudoku.puzzle import SudokuPuzzle

NAME = "Nonconsecutive Sudoku #001"


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 3, 0, 0, 0, 6, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_nonconsecutive_constraints()

    return puzzle
