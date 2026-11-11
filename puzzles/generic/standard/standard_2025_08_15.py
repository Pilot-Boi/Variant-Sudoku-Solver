"""PuzzleMadness Standard Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 6, 0, 0, 3],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 9, 0, 0, 2, 0, 0],
        [0, 6, 1, 0, 0, 0, 3, 0, 0],
        [0, 3, 0, 0, 8, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 1, 4],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 7],
        [0, 0, 9, 0, 7, 1, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
