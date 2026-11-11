"""PuzzleMadness Standard Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 1, 0, 0, 8],
        [7, 0, 0, 0, 9, 0, 0, 6, 0],
        [3, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 0, 9, 0, 0, 2, 0, 0, 0],
        [0, 0, 7, 0, 8, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 6, 9, 0, 1, 0],
        [0, 8, 0, 3, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
