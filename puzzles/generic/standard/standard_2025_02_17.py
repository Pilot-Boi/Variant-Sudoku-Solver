"""PuzzleMadness Standard Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 6, 0, 3, 7],
        [6, 0, 9, 1, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 5],
        [0, 0, 0, 0, 9, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [3, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 9],
        [9, 7, 0, 2, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
