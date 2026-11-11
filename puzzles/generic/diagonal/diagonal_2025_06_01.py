"""PuzzleMadness Diagonal Sudoku — 2025-06-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-06-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/6/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 9, 0, 0],
        [5, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 4, 5, 3, 0],
        [6, 1, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
