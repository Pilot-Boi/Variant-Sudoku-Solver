"""PuzzleMadness Standard Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 6, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [3, 4, 7, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 7, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 5, 0, 8, 0],
        [0, 0, 2, 0, 0, 3, 7, 0, 0],
        [0, 0, 0, 9, 4, 0, 0, 5, 1],
        [0, 0, 1, 0, 0, 6, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
