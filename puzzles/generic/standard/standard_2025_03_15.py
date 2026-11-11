"""PuzzleMadness Standard Sudoku — 2025-03-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 5, 0, 0, 0, 0, 6, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 9, 7, 0, 3, 4, 5, 0],
        [8, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 7, 9, 0],
        [0, 1, 0, 2, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 4, 3],
        [5, 0, 0, 0, 1, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
