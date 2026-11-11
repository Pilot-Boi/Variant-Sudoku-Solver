"""PuzzleMadness Diagonal Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 7, 0, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 3, 8, 0, 0, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 4, 0],
        [9, 0, 0, 0, 0, 0, 5, 1, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 4, 6, 5, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
