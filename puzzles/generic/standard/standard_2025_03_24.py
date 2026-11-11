"""PuzzleMadness Standard Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 2, 1, 0, 8],
        [0, 0, 0, 0, 0, 7, 4, 0, 0],
        [5, 0, 0, 0, 0, 0, 9, 3, 0],
        [0, 4, 0, 7, 0, 0, 0, 6, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 9],
        [6, 0, 2, 8, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 0, 0],
        [4, 5, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
