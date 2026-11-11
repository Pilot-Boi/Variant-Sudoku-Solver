"""PuzzleMadness Diagonal Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 7, 0, 0, 0, 2, 0],
        [0, 0, 0, 1, 6, 0, 3, 9, 0],
        [0, 7, 2, 0, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 5, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 9, 8, 0, 0, 4, 0],
        [7, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
