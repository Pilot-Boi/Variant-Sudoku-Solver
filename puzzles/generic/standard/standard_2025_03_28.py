"""PuzzleMadness Standard Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 6, 9, 4, 0, 0],
        [7, 0, 8, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 8, 4, 5],
        [0, 0, 2, 4, 0, 0, 0, 6, 7],
        [0, 0, 7, 0, 0, 1, 0, 0, 0],
        [0, 5, 0, 0, 3, 0, 9, 0, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
