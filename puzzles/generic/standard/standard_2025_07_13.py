"""PuzzleMadness Standard Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 1, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 3],
        [0, 3, 0, 8, 0, 4, 0, 0, 0],
        [0, 6, 0, 0, 1, 0, 0, 9, 0],
        [2, 0, 0, 0, 9, 7, 0, 4, 8],
        [0, 0, 0, 0, 0, 2, 0, 8, 0],
        [0, 1, 0, 0, 0, 0, 2, 6, 0],
        [0, 0, 8, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
