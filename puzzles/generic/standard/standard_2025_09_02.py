"""PuzzleMadness Standard Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 1, 9, 2, 0, 0, 0],
        [4, 9, 1, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [9, 0, 4, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 2, 0, 0, 6, 5],
        [7, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 2, 6, 5, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
