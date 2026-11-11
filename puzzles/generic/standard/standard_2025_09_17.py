"""PuzzleMadness Standard Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 5, 1, 0, 0, 0],
        [0, 7, 0, 2, 0, 0, 8, 0, 0],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [6, 0, 1, 0, 0, 0, 0, 5, 4],
        [0, 0, 3, 0, 0, 0, 6, 0, 0],
        [0, 2, 0, 5, 0, 0, 3, 7, 0],
        [0, 8, 6, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 8, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
