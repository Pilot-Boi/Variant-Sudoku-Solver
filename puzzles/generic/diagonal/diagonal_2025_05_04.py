"""PuzzleMadness Diagonal Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 3, 7, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 7, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 6, 0, 4, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 4, 0, 0, 0],
        [7, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
