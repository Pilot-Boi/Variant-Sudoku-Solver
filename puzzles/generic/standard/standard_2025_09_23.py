"""PuzzleMadness Standard Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 6, 8, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 1, 0, 0, 6, 0],
        [0, 6, 0, 0, 2, 0, 8, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 5, 0],
        [0, 0, 8, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 2],
        [9, 4, 3, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
