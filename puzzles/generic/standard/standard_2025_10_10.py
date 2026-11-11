"""PuzzleMadness Standard Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 6, 0, 0, 7],
        [0, 0, 3, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 5],
        [2, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 8, 4],
        [6, 0, 0, 4, 0, 0, 0, 0, 0],
        [8, 0, 2, 0, 9, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 7, 0],
        [9, 4, 0, 5, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
