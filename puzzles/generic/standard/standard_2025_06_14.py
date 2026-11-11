"""PuzzleMadness Standard Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 4, 0, 3, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 5],
        [0, 6, 0, 0, 8, 0, 0, 0, 0],
        [6, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 5, 4, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
