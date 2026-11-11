"""PuzzleMadness Standard Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 3, 0, 0, 0, 0, 0, 5],
        [2, 0, 0, 0, 1, 6, 0, 0, 4],
        [0, 0, 8, 3, 0, 9, 0, 0, 0],
        [0, 0, 0, 5, 7, 0, 0, 8, 2],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 9, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 3, 0, 8],
        [3, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
