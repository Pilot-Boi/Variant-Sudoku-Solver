"""PuzzleMadness Standard Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 5],
        [0, 6, 0, 0, 1, 0, 0, 0, 9],
        [0, 7, 0, 0, 0, 0, 3, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 3, 0],
        [0, 0, 0, 6, 0, 0, 0, 8, 0],
        [6, 9, 0, 0, 5, 3, 0, 0, 2],
        [2, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 5, 0, 9, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
