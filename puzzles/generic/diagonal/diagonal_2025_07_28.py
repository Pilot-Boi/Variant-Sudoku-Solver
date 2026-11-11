"""PuzzleMadness Diagonal Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 2, 6, 0, 0],
        [0, 0, 0, 0, 3, 0, 1, 0, 0],
        [0, 0, 0, 4, 5, 0, 0, 6, 0],
        [3, 4, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 9, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 3, 0, 6, 0, 7, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
