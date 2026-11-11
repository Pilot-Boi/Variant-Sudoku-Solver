"""PuzzleMadness Standard Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 8, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 8, 7, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 0, 0],
        [0, 6, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 0, 2],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 9, 3],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
