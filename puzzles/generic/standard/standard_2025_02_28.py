"""PuzzleMadness Standard Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [2, 5, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 4, 9, 0, 0, 0, 3, 0],
        [0, 0, 9, 0, 1, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 7, 1, 0, 0],
        [0, 0, 3, 2, 0, 0, 0, 6, 0],
        [0, 0, 0, 4, 0, 0, 3, 8, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 4],
        [3, 0, 0, 7, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
