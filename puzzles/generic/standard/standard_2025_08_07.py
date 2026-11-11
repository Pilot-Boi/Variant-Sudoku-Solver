"""PuzzleMadness Standard Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 2, 1, 8],
        [0, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 8, 0, 0, 7, 0, 5],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [8, 0, 0, 5, 0, 0, 0, 0, 6],
        [3, 9, 0, 0, 6, 0, 0, 8, 4],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 1, 9, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
