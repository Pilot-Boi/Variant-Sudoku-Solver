"""PuzzleMadness Standard Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 5, 1, 0, 4, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 9, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 8, 0, 7, 2],
        [0, 3, 7, 0, 0, 0, 5, 0, 0],
        [3, 0, 0, 0, 0, 7, 4, 0, 0],
        [0, 0, 8, 0, 0, 2, 0, 9, 7],
        [0, 0, 0, 0, 4, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
