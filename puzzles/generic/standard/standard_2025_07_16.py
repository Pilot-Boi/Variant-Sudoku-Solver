"""PuzzleMadness Standard Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 9, 8, 7],
        [0, 8, 9, 0, 4, 5, 3, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 7, 0, 0, 1, 6],
        [0, 0, 3, 0, 6, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 0, 0],
        [0, 0, 1, 0, 8, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
