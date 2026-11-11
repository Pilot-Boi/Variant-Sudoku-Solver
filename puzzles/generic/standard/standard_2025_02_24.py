"""PuzzleMadness Standard Sudoku — 2025-02-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 1],
        [9, 2, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 3, 5, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 6, 0, 9, 3, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 7, 8, 0, 0, 9, 0, 0],
        [0, 0, 3, 0, 2, 0, 0, 0, 0],
        [5, 9, 0, 3, 0, 0, 0, 1, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
