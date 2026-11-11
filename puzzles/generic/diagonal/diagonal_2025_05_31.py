"""PuzzleMadness Diagonal Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 6, 0, 0, 3, 0, 0, 4, 0],
        [1, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 2, 0, 0, 0, 9, 1],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 9, 5, 8, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
