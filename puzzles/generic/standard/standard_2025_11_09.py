"""PuzzleMadness Standard Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 2, 0, 6],
        [0, 2, 7, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 7, 0, 0, 0, 4],
        [0, 1, 0, 0, 0, 3, 0, 8, 7],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [9, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 6, 0, 7, 3, 0, 0, 4, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
