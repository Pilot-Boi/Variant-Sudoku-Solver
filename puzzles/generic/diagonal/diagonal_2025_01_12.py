"""PuzzleMadness Diagonal Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 6, 1, 0, 3, 2, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 1, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 8, 5, 2, 3, 0, 0],
        [0, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
