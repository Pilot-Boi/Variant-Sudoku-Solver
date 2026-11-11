"""PuzzleMadness Standard Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 8, 0, 0, 3, 2],
        [0, 0, 9, 0, 6, 0, 0, 0, 0],
        [0, 4, 1, 0, 0, 0, 0, 0, 5],
        [8, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 6, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 6, 4, 0, 1, 0, 3],
        [9, 0, 0, 0, 0, 0, 0, 6, 8],
        [0, 1, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
