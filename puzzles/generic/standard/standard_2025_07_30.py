"""PuzzleMadness Standard Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 3, 0, 0, 7, 0],
        [0, 0, 9, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 3, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 8, 7, 0, 2, 3],
        [0, 3, 2, 0, 0, 0, 6, 4, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 5, 0, 2, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
