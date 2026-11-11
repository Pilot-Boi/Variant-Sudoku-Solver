"""PuzzleMadness Standard Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 4, 0, 7, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
        [5, 1, 0, 0, 0, 0, 0, 0, 0],
        [9, 5, 0, 0, 3, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 1, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 8],
        [3, 0, 8, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
