"""PuzzleMadness Standard Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [8, 9, 0, 0, 4, 6, 0, 1, 0],
        [0, 0, 0, 1, 2, 0, 0, 0, 0],
        [3, 0, 7, 0, 0, 0, 0, 6, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 0, 9],
        [7, 4, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [1, 0, 0, 2, 0, 0, 3, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
