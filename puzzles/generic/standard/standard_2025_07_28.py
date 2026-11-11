"""PuzzleMadness Standard Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 8, 2, 0, 7, 0],
        [0, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 9, 0, 7, 0, 1, 0, 0, 3],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 9, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 9],
        [0, 2, 0, 0, 0, 0, 8, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
