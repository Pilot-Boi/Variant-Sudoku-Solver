"""PuzzleMadness Diagonal Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 5, 0],
        [2, 0, 0, 8, 7, 4, 0, 0, 0],
        [0, 8, 3, 0, 5, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 3],
        [8, 0, 9, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
