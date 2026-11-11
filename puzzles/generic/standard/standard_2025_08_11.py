"""PuzzleMadness Standard Sudoku — 2025-08-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 8, 0, 9, 0],
        [4, 0, 5, 0, 6, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 9, 7, 0, 1, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 8, 4, 5, 0, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
