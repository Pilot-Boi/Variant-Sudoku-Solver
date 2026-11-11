"""PuzzleMadness Standard Sudoku — 2025-04-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 9],
        [0, 0, 6, 0, 5, 0, 0, 0, 0],
        [9, 8, 0, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 5, 8, 6, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 3, 0],
        [3, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 9, 0, 4],
        [0, 0, 2, 0, 0, 4, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
