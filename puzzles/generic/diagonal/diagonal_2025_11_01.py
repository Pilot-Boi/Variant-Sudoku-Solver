"""PuzzleMadness Diagonal Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 1, 6, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 8, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 5, 0, 0],
        [0, 8, 0, 2, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 7],
        [0, 4, 7, 6, 0, 0, 1, 3, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
