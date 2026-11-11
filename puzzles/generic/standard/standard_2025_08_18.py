"""PuzzleMadness Standard Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 7, 0, 3, 0, 9],
        [8, 0, 4, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 2, 0, 0, 4],
        [0, 3, 1, 0, 5, 0, 6, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 8, 9, 0, 0, 0],
        [6, 0, 9, 0, 3, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
