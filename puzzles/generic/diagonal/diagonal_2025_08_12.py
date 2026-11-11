"""PuzzleMadness Diagonal Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 6, 9, 7, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 2],
        [0, 0, 0, 4, 0, 8, 0, 0, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 2, 0, 0, 0, 1, 0, 0],
        [1, 0, 5, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 3, 0],
        [8, 0, 0, 0, 0, 5, 6, 0, 0],
        [0, 3, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
