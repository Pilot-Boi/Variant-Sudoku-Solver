"""PuzzleMadness Standard Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 5, 0, 1, 0, 0, 6, 0],
        [0, 0, 0, 7, 0, 8, 0, 2, 3],
        [0, 3, 0, 0, 0, 5, 0, 7, 0],
        [0, 0, 9, 0, 3, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 9],
        [2, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 5, 0, 0],
        [0, 0, 4, 2, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
