"""PuzzleMadness Standard Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 8, 0, 9, 0],
        [9, 0, 0, 0, 1, 0, 0, 0, 6],
        [5, 9, 0, 8, 7, 0, 0, 6, 0],
        [8, 0, 0, 0, 0, 6, 0, 0, 0],
        [6, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 3, 0, 4, 0, 0],
        [1, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
