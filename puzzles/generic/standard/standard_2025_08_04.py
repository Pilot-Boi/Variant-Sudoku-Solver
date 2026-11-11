"""PuzzleMadness Standard Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 9, 4],
        [0, 0, 0, 9, 0, 5, 0, 3, 2],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 2, 0],
        [0, 4, 0, 8, 1, 0, 0, 0, 6],
        [7, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 4, 5, 3, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
