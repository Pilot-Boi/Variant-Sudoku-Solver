"""PuzzleMadness Standard Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 2, 5],
        [0, 6, 0, 0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 8, 0, 3, 9, 0],
        [0, 5, 7, 0, 0, 4, 0, 0, 8],
        [9, 0, 2, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 1, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 5, 0],
        [0, 7, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
