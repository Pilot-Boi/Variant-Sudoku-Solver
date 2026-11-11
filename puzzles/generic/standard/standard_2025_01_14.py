"""PuzzleMadness Standard Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 7, 0, 5, 6, 8, 0],
        [9, 0, 7, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 8, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 4, 0, 0, 0, 7, 0, 0, 5],
        [8, 6, 0, 2, 0, 0, 0, 0, 0],
        [5, 0, 3, 0, 4, 0, 2, 0, 9],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
