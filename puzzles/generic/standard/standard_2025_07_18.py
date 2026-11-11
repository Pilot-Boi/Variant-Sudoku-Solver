"""PuzzleMadness Standard Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 2, 0, 0, 0, 8, 9],
        [0, 0, 0, 0, 6, 0, 0, 0, 7],
        [0, 6, 4, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 5],
        [0, 0, 0, 5, 9, 3, 7, 0, 0],
        [3, 7, 0, 0, 0, 0, 0, 0, 0],
        [5, 9, 0, 0, 0, 4, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
