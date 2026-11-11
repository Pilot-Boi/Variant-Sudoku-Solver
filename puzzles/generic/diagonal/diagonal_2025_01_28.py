"""PuzzleMadness Diagonal Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 1, 5, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 9, 2, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 3, 0],
        [4, 8, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 1, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
