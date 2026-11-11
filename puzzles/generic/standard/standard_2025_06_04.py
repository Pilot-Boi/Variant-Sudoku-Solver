"""PuzzleMadness Standard Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 6, 8, 0, 0, 9, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 4],
        [0, 5, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 5, 9, 3],
        [0, 0, 0, 4, 0, 0, 7, 0, 2],
        [0, 7, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 2, 3, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
