"""PuzzleMadness Standard Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 2],
        [0, 3, 0, 8, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0],
        [2, 5, 0, 0, 0, 0, 3, 8, 0],
        [0, 0, 0, 3, 9, 0, 0, 0, 0],
        [6, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 4, 5, 0, 0, 2, 0],
        [0, 0, 4, 6, 0, 0, 0, 0, 7],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
