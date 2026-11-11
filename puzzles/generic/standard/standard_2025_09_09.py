"""PuzzleMadness Standard Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 1, 0, 0, 0, 0, 0],
        [0, 6, 1, 0, 0, 4, 3, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 2, 0],
        [0, 5, 0, 0, 0, 7, 1, 6, 3],
        [0, 0, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 6, 0, 1, 0, 9, 5],
        [0, 0, 0, 0, 2, 0, 0, 1, 7],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
