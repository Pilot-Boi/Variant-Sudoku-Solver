"""PuzzleMadness Standard Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 6, 9, 0, 5, 0, 0],
        [0, 0, 2, 0, 8, 0, 7, 6, 0],
        [1, 0, 0, 0, 6, 0, 0, 5, 0],
        [3, 0, 0, 0, 0, 2, 9, 0, 0],
        [8, 4, 6, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
