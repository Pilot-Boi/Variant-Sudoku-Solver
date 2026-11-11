"""PuzzleMadness Standard Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 4, 1, 0, 9, 0, 0, 0],
        [0, 0, 3, 0, 8, 0, 0, 5, 9],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 2],
        [9, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [2, 6, 1, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
