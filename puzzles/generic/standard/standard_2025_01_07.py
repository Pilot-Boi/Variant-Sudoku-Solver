"""PuzzleMadness Standard Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 5, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 9, 0, 0, 3],
        [0, 0, 9, 8, 1, 7, 0, 0, 0],
        [1, 6, 5, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 7, 3, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
