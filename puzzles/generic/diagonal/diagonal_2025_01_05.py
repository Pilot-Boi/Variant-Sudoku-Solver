"""PuzzleMadness Diagonal Sudoku — 2025-01-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 3, 0, 4, 0, 2],
        [3, 0, 6, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [1, 4, 3, 9, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 2, 0, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
