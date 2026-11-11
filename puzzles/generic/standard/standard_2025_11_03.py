"""PuzzleMadness Standard Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [3, 0, 4, 0, 6, 0, 7, 0, 0],
        [0, 7, 0, 5, 3, 0, 9, 0, 0],
        [0, 0, 6, 7, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 8, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 2, 0, 1, 0, 0, 9, 0],
        [0, 8, 7, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 7, 3, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
