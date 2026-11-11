"""PuzzleMadness Diagonal Sudoku — 2025-09-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 8, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 4, 0, 3, 0, 2, 9, 0],
        [5, 0, 0, 0, 1, 0, 0, 0, 0],
        [2, 0, 0, 5, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 6, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 9, 0, 0, 0, 5, 3, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
