"""PuzzleMadness Diagonal Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 9, 6, 3, 0, 0, 0, 0],
        [0, 1, 7, 9, 0, 0, 0, 0, 0],
        [0, 0, 4, 1, 0, 0, 3, 0, 0],
        [2, 7, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
