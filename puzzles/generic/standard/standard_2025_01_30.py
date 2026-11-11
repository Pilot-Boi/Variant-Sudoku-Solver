"""PuzzleMadness Standard Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 1, 0, 0, 0, 6, 0],
        [0, 6, 0, 0, 0, 0, 0, 3, 0],
        [8, 1, 0, 0, 2, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 8, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 0, 0, 0, 4, 5, 0, 6],
        [0, 0, 0, 9, 3, 8, 0, 0, 0],
        [1, 0, 0, 2, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
