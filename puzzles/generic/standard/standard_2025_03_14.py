"""PuzzleMadness Standard Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 9, 0, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 4, 3],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 5, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 1, 5],
        [0, 0, 3, 0, 6, 0, 0, 0, 1],
        [5, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 8, 0, 4, 3, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
