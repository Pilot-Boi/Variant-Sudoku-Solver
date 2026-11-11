"""PuzzleMadness Standard Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 3, 4, 9, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 4, 0, 0, 0, 0, 1],
        [3, 0, 0, 0, 1, 9, 0, 7, 0],
        [0, 0, 5, 0, 0, 7, 2, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 3, 9, 0],
        [0, 0, 1, 6, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
