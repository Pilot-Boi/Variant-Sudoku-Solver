"""PuzzleMadness Standard Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 8, 0, 0, 9, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 4, 0, 3, 0, 1, 0],
        [0, 0, 9, 0, 2, 0, 0, 0, 0],
        [7, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 7, 0, 0, 9, 6, 0],
        [0, 0, 0, 1, 0, 0, 8, 0, 0],
        [0, 0, 0, 9, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 6, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
