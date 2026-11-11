"""PuzzleMadness Standard Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 4, 6, 3],
        [0, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 5, 0, 9],
        [0, 0, 0, 0, 8, 0, 0, 5, 0],
        [6, 0, 0, 1, 0, 9, 0, 0, 7],
        [0, 3, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 1, 0, 0],
        [7, 8, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 4, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
