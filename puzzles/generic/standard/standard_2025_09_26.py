"""PuzzleMadness Standard Sudoku — 2025-09-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [9, 0, 7, 0, 0, 0, 0, 5, 0],
        [0, 0, 3, 0, 6, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 5],
        [2, 8, 0, 0, 1, 0, 0, 0, 0],
        [0, 5, 1, 8, 0, 0, 0, 0, 9],
        [5, 0, 0, 0, 4, 0, 0, 6, 1],
        [0, 0, 0, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
