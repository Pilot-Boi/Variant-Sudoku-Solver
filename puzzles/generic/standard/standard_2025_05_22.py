"""PuzzleMadness Standard Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [7, 8, 4, 0, 1, 0, 0, 2, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 3],
        [9, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 6, 1, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 7, 0, 6, 3, 0, 0, 8],
        [0, 0, 0, 5, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
