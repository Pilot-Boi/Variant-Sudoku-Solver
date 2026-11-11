"""PuzzleMadness Standard Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 2, 5, 0, 1, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 1, 0, 9, 8],
        [0, 0, 4, 0, 0, 6, 3, 0, 0],
        [6, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 7, 8, 6, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [8, 9, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
