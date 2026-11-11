"""PuzzleMadness Standard Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 4, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 1, 0, 5],
        [2, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 6, 0, 5, 0, 7, 2, 9],
        [0, 0, 5, 0, 0, 3, 6, 0, 0],
        [0, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 3, 7, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
