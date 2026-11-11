"""PuzzleMadness Standard Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 1, 0, 0, 0, 0],
        [9, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 0, 6, 0, 0, 7, 2, 0],
        [4, 0, 0, 0, 0, 0, 0, 9, 1],
        [0, 0, 0, 0, 4, 7, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 8, 0],
        [8, 0, 0, 5, 2, 0, 0, 0, 3],
        [6, 1, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
