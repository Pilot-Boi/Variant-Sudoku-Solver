"""PuzzleMadness Standard Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 4, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 6, 4, 0, 0, 1, 0],
        [4, 0, 0, 0, 0, 7, 3, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 8, 0],
        [0, 0, 3, 8, 5, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [1, 7, 0, 0, 0, 6, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
