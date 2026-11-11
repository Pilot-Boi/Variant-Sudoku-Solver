"""PuzzleMadness Standard Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 8, 2, 0],
        [0, 8, 0, 0, 4, 3, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 1, 4, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 3],
        [1, 0, 0, 0, 0, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [0, 0, 5, 0, 0, 0, 7, 8, 9],
        [6, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
