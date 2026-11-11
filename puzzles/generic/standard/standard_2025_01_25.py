"""PuzzleMadness Standard Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 2, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 8, 0, 3, 0, 0, 4, 1],
        [0, 0, 0, 8, 0, 7, 0, 3, 0],
        [0, 9, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 0, 4, 0, 0, 0, 7, 9],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 4, 6, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
