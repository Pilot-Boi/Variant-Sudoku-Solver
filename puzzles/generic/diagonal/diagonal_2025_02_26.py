"""PuzzleMadness Diagonal Sudoku — 2025-02-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-02-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/2/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 2, 3],
        [0, 2, 0, 5, 1, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [6, 5, 0, 0, 2, 0, 8, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 9, 0, 3, 0, 8, 0],
        [0, 0, 0, 0, 0, 1, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
