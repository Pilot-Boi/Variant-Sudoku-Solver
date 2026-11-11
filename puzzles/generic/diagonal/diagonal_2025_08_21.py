"""PuzzleMadness Diagonal Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 2, 1, 7, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [4, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 0, 2, 8, 0, 4, 0],
        [0, 4, 0, 5, 0, 0, 6, 9, 0],
        [0, 0, 0, 0, 0, 9, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
