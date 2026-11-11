"""PuzzleMadness Standard Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 3, 0],
        [6, 1, 0, 0, 0, 8, 0, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 0, 4],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 8, 0, 9, 7, 0, 2, 0, 5],
        [7, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 8, 0, 0, 4, 7],
        [0, 4, 1, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 9, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
