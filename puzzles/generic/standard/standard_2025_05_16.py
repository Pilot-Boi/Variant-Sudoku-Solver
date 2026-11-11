"""PuzzleMadness Standard Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 7, 0, 0, 8, 0, 0],
        [0, 9, 0, 4, 0, 0, 0, 0, 7],
        [0, 7, 4, 0, 1, 0, 0, 5, 0],
        [0, 2, 0, 0, 0, 3, 7, 0, 8],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 9, 4, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 5, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
