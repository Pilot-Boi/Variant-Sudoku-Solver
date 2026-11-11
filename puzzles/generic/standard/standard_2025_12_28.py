"""PuzzleMadness Standard Sudoku — 2025-12-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 7, 3, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 4, 0, 0, 5, 0, 0, 1, 6],
        [0, 0, 3, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 8],
        [6, 0, 9, 7, 1, 0, 3, 4, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
