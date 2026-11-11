"""PuzzleMadness Standard Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 9, 0, 0],
        [8, 0, 0, 6, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 0, 7, 3, 1],
        [0, 0, 1, 5, 2, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 3, 7, 0, 0, 8, 0, 4, 0],
        [9, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
