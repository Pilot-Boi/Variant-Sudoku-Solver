"""PuzzleMadness Standard Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 2, 4, 7, 0, 9, 0, 0],
        [0, 8, 1, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [9, 0, 5, 0, 0, 1, 6, 0, 4],
        [1, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 4, 9, 0, 0, 0, 0, 3],
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
