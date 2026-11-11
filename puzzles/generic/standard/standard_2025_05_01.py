"""PuzzleMadness Standard Sudoku — 2025-05-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 4, 0, 0, 2],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 8, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 2, 9, 0],
        [0, 8, 7, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 1, 0],
        [1, 0, 5, 0, 0, 0, 6, 0, 4],
        [3, 0, 0, 4, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
