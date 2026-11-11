"""PuzzleMadness Standard Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 1, 0, 0, 0, 0, 8, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 7, 5, 0, 0, 0, 1, 0, 8],
        [0, 0, 9, 0, 0, 0, 0, 6, 0],
        [0, 2, 0, 5, 0, 7, 0, 0, 0],
        [0, 9, 0, 0, 0, 6, 0, 0, 0],
        [2, 0, 0, 0, 0, 4, 0, 0, 0],
        [8, 0, 1, 0, 0, 0, 6, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
