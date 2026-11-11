"""PuzzleMadness Standard Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 3, 0, 4, 0, 6, 0, 0, 0],
        [2, 0, 6, 3, 0, 5, 0, 8, 0],
        [0, 0, 1, 0, 2, 0, 0, 6, 0],
        [0, 0, 0, 8, 0, 0, 4, 0, 0],
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 1, 0, 0],
        [0, 9, 4, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 9, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
