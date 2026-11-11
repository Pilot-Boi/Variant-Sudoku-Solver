"""PuzzleMadness Diagonal Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 8],
        [0, 0, 1, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 5],
        [1, 0, 2, 0, 5, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 6, 0, 0, 3, 0, 2, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
