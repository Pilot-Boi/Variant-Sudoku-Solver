"""PuzzleMadness Standard Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 7, 9, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 4, 0, 0, 0, 1, 0],
        [0, 1, 9, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 5, 6, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 7, 2, 0, 8, 0, 9, 0, 0],
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 4, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
