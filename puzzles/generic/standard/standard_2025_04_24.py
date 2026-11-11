"""PuzzleMadness Standard Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 2, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 2, 4],
        [9, 8, 5, 0, 7, 0, 0, 0, 0],
        [0, 3, 0, 0, 5, 0, 0, 0, 0],
        [2, 0, 0, 3, 0, 0, 0, 6, 0],
        [0, 4, 3, 2, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 5, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
