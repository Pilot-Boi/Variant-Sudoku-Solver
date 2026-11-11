"""PuzzleMadness Diagonal Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 6, 0, 4, 0],
        [0, 0, 0, 7, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 0, 0, 3, 1, 0],
        [0, 0, 1, 5, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [9, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
