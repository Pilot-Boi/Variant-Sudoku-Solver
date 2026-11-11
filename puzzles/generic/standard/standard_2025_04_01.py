"""PuzzleMadness Standard Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 8, 0, 0, 0, 2, 0, 0, 0],
        [4, 0, 0, 9, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 4, 6, 0, 0, 8],
        [8, 9, 0, 0, 3, 0, 1, 0, 4],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 3, 7, 0, 0, 6, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 5],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
