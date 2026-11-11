"""PuzzleMadness Standard Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 4, 5, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
        [0, 0, 0, 0, 7, 6, 0, 1, 3],
        [5, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 9, 3, 0, 0, 0, 2, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 3, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
