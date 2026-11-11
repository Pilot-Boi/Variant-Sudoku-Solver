"""PuzzleMadness Standard Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 1, 3, 5, 0],
        [0, 0, 0, 0, 7, 0, 0, 2, 0],
        [1, 0, 0, 6, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 9, 0],
        [0, 0, 1, 2, 0, 0, 7, 3, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 5],
        [0, 6, 0, 0, 9, 0, 0, 0, 7],
        [0, 2, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
