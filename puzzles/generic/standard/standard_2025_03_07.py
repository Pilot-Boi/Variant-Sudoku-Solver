"""PuzzleMadness Standard Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 5],
        [4, 0, 0, 0, 0, 3, 9, 0, 0],
        [0, 0, 6, 0, 8, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 3, 4, 0, 9, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 8, 0, 5, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 8, 2, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
