"""PuzzleMadness Standard Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 5, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 2, 7, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 3, 0, 6],
        [7, 0, 0, 0, 3, 0, 0, 0, 0],
        [9, 0, 2, 0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 4, 2, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
