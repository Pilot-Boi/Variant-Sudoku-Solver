"""PuzzleMadness Standard Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 7, 6, 0, 0, 0, 0],
        [0, 0, 4, 0, 5, 9, 3, 0, 0],
        [0, 6, 0, 8, 0, 0, 0, 9, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 3, 0, 0, 0, 2, 0, 0, 0],
        [7, 0, 1, 0, 0, 3, 9, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 5, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
