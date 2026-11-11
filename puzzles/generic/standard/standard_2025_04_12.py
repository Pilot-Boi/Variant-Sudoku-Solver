"""PuzzleMadness Standard Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 8, 0, 5],
        [6, 0, 0, 9, 0, 0, 0, 7, 0],
        [5, 4, 0, 0, 0, 0, 0, 0, 6],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 1, 2],
        [0, 0, 4, 2, 5, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 7, 0, 3, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
