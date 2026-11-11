"""PuzzleMadness Diagonal Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 8, 0, 0, 1, 7, 0, 9],
        [0, 0, 0, 0, 0, 5, 2, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 6],
        [1, 0, 0, 3, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
