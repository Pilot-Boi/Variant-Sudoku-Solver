"""PuzzleMadness Standard Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 9, 0, 6],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 5, 7, 8],
        [0, 0, 4, 5, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [1, 9, 0, 0, 0, 7, 0, 8, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 4],
        [2, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
