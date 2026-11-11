"""PuzzleMadness Standard Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 2, 0, 0, 0, 3],
        [0, 7, 0, 8, 0, 5, 0, 9, 0],
        [5, 0, 9, 0, 7, 8, 0, 4, 1],
        [0, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
        [4, 0, 8, 6, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
