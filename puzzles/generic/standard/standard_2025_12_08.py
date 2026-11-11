"""PuzzleMadness Standard Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 6, 2, 0, 1, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [4, 1, 0, 7, 0, 5, 8, 0, 0],
        [0, 0, 0, 0, 0, 4, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 1, 0, 2, 8],
        [0, 0, 0, 0, 8, 0, 0, 0, 9],
        [1, 0, 0, 3, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
