"""PuzzleMadness Diagonal Sudoku — 2025-10-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [9, 1, 3, 2, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 6, 4],
        [7, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
