"""PuzzleMadness Diagonal Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 5, 3, 0],
        [0, 5, 0, 6, 0, 8, 2, 0, 0],
        [2, 0, 0, 0, 0, 0, 7, 6, 0],
        [0, 0, 5, 7, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 4, 6, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
