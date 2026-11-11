"""PuzzleMadness Standard Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 1, 0, 3, 0, 4],
        [6, 0, 0, 0, 0, 0, 8, 7, 9],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 3, 0, 5, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 6, 0, 4, 9, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 3, 0, 0, 0, 0, 1],
        [0, 0, 0, 6, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
