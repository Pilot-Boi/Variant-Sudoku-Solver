"""PuzzleMadness Standard Sudoku — 2025-12-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 2, 0, 3],
        [0, 0, 0, 6, 0, 8, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 5, 4, 0, 0, 0, 0],
        [2, 5, 6, 7, 0, 0, 4, 0, 0],
        [0, 4, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 5],
        [8, 2, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
