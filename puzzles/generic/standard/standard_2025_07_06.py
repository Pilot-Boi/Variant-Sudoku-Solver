"""PuzzleMadness Standard Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 0, 0],
        [3, 1, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 8, 9, 0, 0, 3, 1],
        [0, 9, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 3, 0, 0, 0, 6, 2, 0],
        [4, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 3, 0, 0, 4, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
