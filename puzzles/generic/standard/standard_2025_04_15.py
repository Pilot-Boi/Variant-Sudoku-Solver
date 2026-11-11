"""PuzzleMadness Standard Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 7, 1, 8, 0],
        [9, 0, 0, 0, 0, 0, 0, 3, 5],
        [1, 0, 3, 0, 5, 9, 2, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 3, 0, 0],
        [0, 0, 2, 6, 3, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
