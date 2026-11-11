"""PuzzleMadness Standard Sudoku — 2025-05-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 8, 0, 5],
        [5, 7, 0, 2, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 9, 0, 2, 0, 3],
        [0, 0, 6, 0, 8, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 9, 0, 6, 5, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
