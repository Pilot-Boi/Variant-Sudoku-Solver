"""PuzzleMadness Diagonal Sudoku — 2025-09-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 6, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 4, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 6],
        [7, 5, 9, 0, 6, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
