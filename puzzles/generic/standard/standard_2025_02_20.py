"""PuzzleMadness Standard Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 9, 0, 5, 0],
        [9, 0, 8, 0, 0, 0, 0, 2, 0],
        [6, 0, 7, 5, 0, 0, 0, 0, 0],
        [0, 2, 4, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 9, 4, 2, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 1, 6, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [8, 0, 2, 7, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
