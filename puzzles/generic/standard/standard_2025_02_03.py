"""PuzzleMadness Standard Sudoku — 2025-02-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 3, 0, 6, 0, 0, 2, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 4, 0, 0, 1, 8, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 2, 3, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 1, 0, 0, 2, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
