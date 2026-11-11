"""PuzzleMadness Standard Sudoku — 2025-09-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 3, 9],
        [0, 8, 2, 4, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 7, 1, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 7, 0],
        [8, 3, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 2, 0, 0, 0, 6],
        [5, 7, 0, 0, 0, 0, 6, 0, 3],
        [0, 0, 9, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
