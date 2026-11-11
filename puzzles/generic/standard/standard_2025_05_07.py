"""PuzzleMadness Standard Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [2, 9, 1, 5, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 4, 6, 0, 0],
        [0, 5, 0, 8, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 6, 0, 0, 2],
        [6, 0, 8, 4, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
