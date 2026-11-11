"""PuzzleMadness Standard Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0, 5],
        [3, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 4, 5, 0, 0, 3, 2, 0, 0],
        [0, 0, 6, 4, 9, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 2, 0, 5, 4, 0, 8, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
