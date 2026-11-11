"""PuzzleMadness Standard Sudoku — 2025-10-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-10-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/10/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 3, 7, 0],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 8, 9, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 7, 0, 8, 4, 0, 0, 0],
        [0, 0, 3, 5, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 7, 5, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 9],
        [0, 7, 8, 0, 3, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
