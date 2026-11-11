"""PuzzleMadness Standard Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 1, 0, 0, 2, 4, 0, 0, 6],
        [0, 0, 5, 0, 0, 0, 9, 0, 0],
        [2, 0, 0, 0, 0, 0, 8, 9, 0],
        [0, 0, 3, 0, 0, 0, 5, 0, 0],
        [0, 8, 0, 1, 0, 7, 0, 4, 0],
        [0, 0, 2, 4, 9, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
