"""PuzzleMadness Standard Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 5],
        [0, 5, 0, 0, 0, 7, 9, 0, 4],
        [0, 0, 4, 0, 3, 6, 0, 0, 0],
        [0, 0, 6, 1, 5, 0, 3, 0, 0],
        [3, 0, 0, 9, 0, 0, 1, 0, 0],
        [9, 7, 0, 6, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 9],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
