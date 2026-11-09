from sudoku.puzzle import SudokuPuzzle

NAME = "Anti-King Sudoku #001"


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 4],
        [0, 0, 1, 2, 3, 0, 0, 6, 0],
        [0, 0, 8, 0, 4, 0, 0, 0, 0],
        [8, 0, 7, 6, 5, 0, 1, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 2, 0, 8, 7, 6, 0, 5],
        [0, 0, 0, 0, 1, 0, 5, 0, 0],
        [0, 7, 0, 0, 2, 3, 4, 0, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_anti_king_constraints()

    return puzzle