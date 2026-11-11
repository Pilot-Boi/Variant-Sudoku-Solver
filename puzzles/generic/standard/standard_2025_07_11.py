"""PuzzleMadness Standard Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 2, 1, 6, 0],
        [0, 0, 8, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 6, 7, 9, 0],
        [1, 0, 9, 0, 0, 0, 0, 7, 0],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 9, 6, 8, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
