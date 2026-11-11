"""PuzzleMadness Standard Sudoku — 2025-09-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 8, 0, 1, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 8, 9, 4, 6, 0, 0, 7],
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [0, 0, 2, 4, 1, 8, 5, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
