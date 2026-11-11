"""PuzzleMadness Diagonal Sudoku — 2025-08-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-08-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/8/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 7, 0, 9, 0, 0],
        [7, 0, 1, 4, 8, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 8],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [8, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
