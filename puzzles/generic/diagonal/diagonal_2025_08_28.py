"""PuzzleMadness Diagonal Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 6, 0, 0, 0, 0, 0, 8],
        [5, 0, 7, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 6, 1, 0, 0],
        [0, 6, 0, 0, 9, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 8, 0, 0, 6, 0, 3, 0, 5],
        [0, 0, 0, 0, 8, 0, 9, 0, 0],
        [0, 0, 0, 0, 1, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
