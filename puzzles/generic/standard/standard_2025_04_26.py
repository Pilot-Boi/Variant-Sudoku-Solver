"""PuzzleMadness Standard Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 6, 5, 0],
        [0, 2, 0, 0, 9, 0, 0, 0, 0],
        [7, 0, 3, 0, 1, 5, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 5, 0, 3, 0, 0, 6, 1],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
