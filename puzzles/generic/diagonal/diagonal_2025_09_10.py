"""PuzzleMadness Diagonal Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 7, 8, 0, 0, 3, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 9, 5, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 6, 0, 1],
        [6, 0, 0, 1, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
