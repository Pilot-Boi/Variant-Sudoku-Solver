"""PuzzleMadness Diagonal Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 4, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 3, 0],
        [8, 0, 4, 1, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 2, 7, 0, 9],
        [0, 0, 8, 4, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
