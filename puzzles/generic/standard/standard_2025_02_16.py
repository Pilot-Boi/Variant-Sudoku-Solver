"""PuzzleMadness Standard Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 0, 4, 0],
        [0, 5, 0, 0, 9, 6, 0, 0, 8],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 3, 0, 6, 0, 0],
        [4, 9, 0, 0, 0, 2, 3, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 8, 0, 7, 5],
        [0, 2, 0, 0, 0, 9, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
