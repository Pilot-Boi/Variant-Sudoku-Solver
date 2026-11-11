"""PuzzleMadness Standard Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 2, 0, 0],
        [0, 2, 0, 6, 1, 5, 3, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 4, 9],
        [0, 0, 0, 0, 6, 4, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 9, 5],
        [0, 0, 0, 0, 0, 0, 7, 0, 3],
        [5, 0, 4, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
