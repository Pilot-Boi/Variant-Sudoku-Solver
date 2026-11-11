"""PuzzleMadness Standard Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 2, 6, 0],
        [0, 3, 0, 8, 0, 0, 7, 9, 0],
        [9, 0, 2, 0, 7, 0, 0, 0, 0],
        [8, 0, 0, 1, 0, 2, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 5],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 2, 5, 0, 8, 0, 0],
        [3, 5, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
