"""PuzzleMadness Standard Sudoku — 2025-09-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 9, 0],
        [1, 0, 0, 8, 6, 0, 0, 0, 4],
        [4, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 2, 0, 6, 0],
        [0, 0, 0, 0, 5, 0, 0, 3, 7],
        [0, 3, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 6, 3, 0, 0],
        [0, 0, 0, 9, 0, 4, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
