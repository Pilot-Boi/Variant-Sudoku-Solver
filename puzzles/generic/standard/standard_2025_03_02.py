"""PuzzleMadness Standard Sudoku — 2025-03-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 3, 0],
        [0, 6, 9, 0, 5, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 4, 0, 0, 8],
        [0, 0, 2, 0, 0, 9, 6, 0, 7],
        [0, 1, 8, 0, 2, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 7, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
