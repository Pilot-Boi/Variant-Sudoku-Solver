"""PuzzleMadness Standard Sudoku — 2025-01-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-01-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/1/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 7, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 3],
        [1, 0, 0, 0, 0, 4, 0, 0, 5],
        [0, 2, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 8, 7, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 9, 2],
        [0, 0, 5, 0, 7, 0, 0, 0, 0],
        [0, 8, 2, 0, 0, 3, 6, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
