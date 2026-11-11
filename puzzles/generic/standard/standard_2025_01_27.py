"""PuzzleMadness Standard Sudoku — 2025-01-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 9, 0, 0, 0, 3, 0],
        [0, 0, 4, 0, 2, 0, 0, 0, 0],
        [9, 0, 0, 2, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 7, 8, 0, 0],
        [0, 6, 7, 0, 0, 1, 4, 0, 0],
        [0, 0, 0, 7, 3, 0, 0, 0, 2],
        [2, 0, 0, 8, 6, 0, 0, 7, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
