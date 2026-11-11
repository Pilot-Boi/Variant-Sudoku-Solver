"""PuzzleMadness Standard Sudoku — 2025-07-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 5, 0, 8, 0, 0],
        [0, 0, 6, 4, 0, 0, 5, 0, 0],
        [3, 1, 0, 0, 6, 0, 0, 9, 0],
        [7, 6, 0, 0, 0, 0, 0, 8, 1],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 0, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 0, 3, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
