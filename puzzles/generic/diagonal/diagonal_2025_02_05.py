"""PuzzleMadness Diagonal Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 6, 0, 4, 0],
        [0, 0, 0, 2, 5, 0, 0, 0, 0],
        [0, 0, 2, 0, 3, 0, 8, 5, 6],
        [0, 1, 3, 0, 0, 0, 0, 0, 0],
        [9, 0, 5, 0, 4, 0, 2, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
