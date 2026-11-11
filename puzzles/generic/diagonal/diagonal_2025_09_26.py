"""PuzzleMadness Diagonal Sudoku — 2025-09-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 9, 0, 0, 4, 2, 0],
        [0, 0, 0, 0, 7, 3, 6, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 9, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
