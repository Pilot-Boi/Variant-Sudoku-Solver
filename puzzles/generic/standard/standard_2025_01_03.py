"""PuzzleMadness Standard Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 3, 7, 0, 1, 2],
        [0, 0, 0, 0, 8, 0, 0, 0, 7],
        [5, 0, 0, 0, 2, 1, 0, 6, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 3, 1, 0, 0, 4, 0, 0],
        [9, 0, 6, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 2, 0],
        [0, 8, 0, 9, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
