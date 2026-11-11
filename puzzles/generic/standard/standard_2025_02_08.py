"""PuzzleMadness Standard Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 2, 0, 0, 0, 0, 6],
        [8, 0, 0, 0, 7, 9, 0, 0, 0],
        [0, 0, 1, 8, 0, 2, 5, 0, 0],
        [0, 0, 7, 5, 0, 0, 3, 0, 1],
        [0, 5, 6, 0, 0, 0, 0, 0, 8],
        [0, 6, 0, 0, 0, 0, 9, 0, 7],
        [0, 0, 0, 0, 5, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
