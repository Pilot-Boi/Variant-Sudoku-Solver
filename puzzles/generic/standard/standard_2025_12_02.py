"""PuzzleMadness Standard Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 5, 0, 8, 4, 7, 2],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [4, 7, 0, 1, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 1],
        [0, 9, 0, 0, 0, 6, 0, 0, 0],
        [0, 1, 0, 7, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 3, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 4, 8],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
