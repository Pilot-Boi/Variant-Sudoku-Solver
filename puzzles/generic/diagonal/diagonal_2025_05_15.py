"""PuzzleMadness Diagonal Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 3, 0, 0, 0, 0],
        [1, 0, 0, 2, 7, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 2, 0, 7, 0, 0, 9, 1, 0],
        [5, 0, 3, 0, 0, 0, 2, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
