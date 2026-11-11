"""PuzzleMadness Standard Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 5, 7, 8, 0, 0, 0, 4],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 3, 5, 4, 0, 0, 0, 0],
        [1, 5, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 5, 6, 0],
        [0, 0, 7, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
