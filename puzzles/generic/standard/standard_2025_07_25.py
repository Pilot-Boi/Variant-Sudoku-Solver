"""PuzzleMadness Standard Sudoku — 2025-07-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 7],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 3, 9],
        [0, 0, 0, 0, 0, 4, 1, 0, 0],
        [0, 1, 6, 0, 0, 0, 0, 4, 0],
        [0, 0, 9, 0, 0, 8, 6, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 4, 0, 0, 5, 0, 3, 1, 8],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
