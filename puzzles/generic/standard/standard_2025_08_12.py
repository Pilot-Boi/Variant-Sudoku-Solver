"""PuzzleMadness Standard Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 4, 1, 0, 9, 0, 0],
        [0, 0, 0, 7, 0, 5, 0, 0, 0],
        [7, 1, 0, 0, 0, 0, 0, 5, 4],
        [4, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 5, 6, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 1, 0, 0, 4, 0, 6],
        [0, 0, 0, 0, 9, 3, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
