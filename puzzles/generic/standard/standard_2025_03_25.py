"""PuzzleMadness Standard Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 8, 0, 0, 1],
        [4, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 1, 0, 0, 0, 5],
        [9, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 0, 0, 0, 7],
        [0, 1, 0, 0, 5, 3, 0, 0, 0],
        [0, 0, 3, 8, 4, 0, 6, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 7, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
