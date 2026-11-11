"""PuzzleMadness Standard Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 7, 0, 1, 0, 0, 8, 0, 2],
        [0, 0, 8, 0, 0, 5, 4, 3, 0],
        [6, 0, 5, 0, 0, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 0, 3],
        [3, 0, 0, 4, 1, 6, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
