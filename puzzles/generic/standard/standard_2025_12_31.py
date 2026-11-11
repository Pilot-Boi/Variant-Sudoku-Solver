"""PuzzleMadness Standard Sudoku — 2025-12-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 1, 8, 0, 0, 0],
        [0, 0, 5, 0, 9, 3, 4, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 6, 0, 0, 0, 0],
        [6, 0, 7, 2, 0, 0, 0, 5, 0],
        [0, 6, 0, 0, 0, 1, 8, 0, 7],
        [5, 4, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
