"""PuzzleMadness Standard Sudoku — 2025-06-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 4, 7, 6],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [5, 4, 0, 0, 6, 0, 0, 0, 0],
        [0, 6, 0, 4, 0, 0, 5, 0, 0],
        [0, 3, 0, 0, 0, 0, 9, 4, 0],
        [0, 0, 0, 0, 5, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 5],
        [0, 0, 0, 0, 2, 1, 0, 0, 0],
        [1, 0, 6, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
