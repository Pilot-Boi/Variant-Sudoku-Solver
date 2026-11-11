"""PuzzleMadness Standard Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 6, 7, 0],
        [0, 0, 0, 4, 8, 0, 3, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 5, 9],
        [0, 8, 0, 0, 0, 5, 7, 0, 2],
        [8, 0, 1, 0, 7, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 4, 0],
        [2, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
