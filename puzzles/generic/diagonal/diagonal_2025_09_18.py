"""PuzzleMadness Diagonal Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 9],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 1],
        [7, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 8, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 4, 8, 0, 1, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
