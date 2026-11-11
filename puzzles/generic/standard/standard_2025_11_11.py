"""PuzzleMadness Standard Sudoku — 2025-11-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 9, 0],
        [5, 0, 1, 4, 0, 0, 2, 0, 0],
        [9, 0, 8, 0, 0, 0, 0, 0, 1],
        [4, 5, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 6, 0, 5, 0, 0],
        [0, 0, 0, 9, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 3, 0],
        [8, 0, 2, 5, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
