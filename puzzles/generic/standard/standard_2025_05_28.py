"""PuzzleMadness Standard Sudoku — 2025-05-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 6, 7, 0, 0],
        [0, 0, 2, 4, 0, 7, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 0, 5, 0, 3, 6, 0],
        [9, 0, 0, 7, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 5, 0, 9, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 2, 0, 0, 5, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
