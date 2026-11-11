"""PuzzleMadness Standard Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 1, 0, 0, 5],
        [6, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [4, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 3, 2, 0, 0, 0],
        [0, 2, 0, 8, 4, 0, 0, 5, 9],
        [0, 0, 8, 0, 0, 0, 0, 3, 6],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
