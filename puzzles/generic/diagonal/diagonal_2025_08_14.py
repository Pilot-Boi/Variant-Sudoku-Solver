"""PuzzleMadness Diagonal Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 7, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 5],
        [2, 0, 8, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 0, 4, 0, 0, 8, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
