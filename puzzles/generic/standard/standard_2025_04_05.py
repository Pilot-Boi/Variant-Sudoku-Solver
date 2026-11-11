"""PuzzleMadness Standard Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [5, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 4, 0, 3, 2, 0, 0, 7],
        [9, 0, 0, 4, 0, 0, 0, 0, 8],
        [8, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 3, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 9, 0, 0],
        [0, 0, 0, 1, 4, 0, 5, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 1, 3],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
