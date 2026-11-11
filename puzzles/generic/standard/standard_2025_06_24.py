"""PuzzleMadness Standard Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 5, 7, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 3, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 2, 0, 0, 0, 5],
        [2, 0, 0, 0, 0, 4, 9, 1, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [5, 0, 0, 0, 6, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 3, 0, 9, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
