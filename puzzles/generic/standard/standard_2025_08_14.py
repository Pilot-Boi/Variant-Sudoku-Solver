"""PuzzleMadness Standard Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 8, 0, 1, 7, 0],
        [5, 0, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 4, 2, 0, 9, 0, 0, 0],
        [8, 0, 0, 9, 4, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 3],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 1, 0, 0, 0, 5, 8],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
