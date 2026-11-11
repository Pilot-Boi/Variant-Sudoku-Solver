"""PuzzleMadness Diagonal Sudoku — 2025-03-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 1, 0, 0, 4, 0, 0, 0],
        [9, 0, 0, 0, 0, 7, 2, 6, 0],
        [1, 4, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 8, 0, 0, 9, 0],
        [7, 9, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
