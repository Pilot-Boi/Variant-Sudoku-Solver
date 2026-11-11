"""PuzzleMadness Standard Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 2, 1, 0, 7, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [3, 1, 0, 0, 7, 0, 4, 9, 0],
        [0, 4, 0, 0, 6, 9, 0, 0, 0],
        [0, 9, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
