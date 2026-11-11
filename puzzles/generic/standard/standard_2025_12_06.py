"""PuzzleMadness Standard Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 7, 3, 0],
        [5, 1, 0, 0, 8, 0, 0, 0, 9],
        [0, 0, 0, 5, 0, 0, 0, 2, 0],
        [0, 0, 9, 0, 0, 4, 0, 8, 0],
        [0, 0, 5, 4, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 1],
        [6, 0, 0, 8, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
