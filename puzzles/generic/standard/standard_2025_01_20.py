"""PuzzleMadness Standard Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [6, 0, 7, 3, 0, 0, 0, 0, 5],
        [0, 1, 0, 0, 7, 0, 0, 0, 0],
        [0, 4, 9, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [3, 2, 0, 0, 8, 0, 6, 0, 0],
        [7, 0, 0, 9, 5, 3, 0, 6, 1],
        [0, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
