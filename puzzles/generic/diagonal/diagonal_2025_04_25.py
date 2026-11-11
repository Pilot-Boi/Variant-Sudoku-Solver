"""PuzzleMadness Diagonal Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 2, 4, 7, 0, 0, 1, 3],
        [3, 0, 0, 0, 0, 5, 0, 0, 0],
        [6, 0, 0, 0, 8, 9, 0, 0, 0],
        [0, 1, 0, 0, 4, 0, 9, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
