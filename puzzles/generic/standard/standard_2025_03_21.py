"""PuzzleMadness Standard Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 5, 0, 9, 1, 3, 7, 0, 0],
        [0, 7, 0, 4, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 9, 0, 1, 4, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 2, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 0, 5, 0],
        [0, 3, 8, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
