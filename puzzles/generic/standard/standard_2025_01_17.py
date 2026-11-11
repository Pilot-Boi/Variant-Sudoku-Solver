"""PuzzleMadness Standard Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 9, 8, 6],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [7, 0, 0, 0, 1, 6, 0, 0, 0],
        [0, 6, 5, 0, 0, 0, 0, 0, 4],
        [9, 0, 0, 0, 4, 0, 8, 2, 0],
        [4, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 8, 0, 9, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
