"""PuzzleMadness Diagonal Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 7, 0, 0, 0, 0],
        [4, 0, 3, 0, 0, 2, 8, 0, 0],
        [7, 1, 0, 0, 0, 0, 2, 5, 6],
        [0, 0, 0, 0, 0, 5, 0, 0, 9],
        [8, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 1, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
