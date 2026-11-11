"""PuzzleMadness Diagonal Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [6, 3, 0, 0, 0, 0, 0, 0, 8],
        [8, 2, 0, 0, 0, 3, 0, 0, 0],
        [0, 9, 7, 0, 6, 8, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
