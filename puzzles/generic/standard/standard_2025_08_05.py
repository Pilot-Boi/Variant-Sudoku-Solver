"""PuzzleMadness Standard Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 6, 2, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 9, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 6, 8, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 1, 0, 5],
        [4, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 1, 0, 0, 7, 8],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
