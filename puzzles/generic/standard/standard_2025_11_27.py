"""PuzzleMadness Standard Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 2, 0, 0, 4, 3, 0, 7, 0],
        [0, 0, 0, 0, 0, 5, 1, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 4, 1, 0, 7, 0, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [9, 0, 3, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 5],
        [0, 0, 0, 0, 9, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
