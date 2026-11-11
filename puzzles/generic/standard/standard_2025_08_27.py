"""PuzzleMadness Standard Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 2, 0, 7, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 5, 0, 0, 2, 4, 0],
        [0, 0, 0, 0, 3, 0, 1, 0, 0],
        [3, 6, 0, 7, 0, 0, 0, 0, 9],
        [0, 8, 0, 0, 5, 4, 0, 0, 0],
        [0, 0, 6, 9, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 4, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
