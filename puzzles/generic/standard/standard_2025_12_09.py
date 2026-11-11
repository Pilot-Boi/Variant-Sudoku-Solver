"""PuzzleMadness Standard Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 2, 6],
        [0, 0, 0, 0, 5, 0, 8, 7, 0],
        [2, 0, 0, 0, 0, 8, 0, 6, 7],
        [1, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 9, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 7, 1, 0],
        [4, 0, 5, 0, 0, 1, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
