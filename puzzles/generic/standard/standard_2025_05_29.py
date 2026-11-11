"""PuzzleMadness Standard Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 1, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 0, 4, 5, 0, 0, 0],
        [0, 9, 7, 6, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 8, 0, 0, 5, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 8, 2],
        [0, 5, 3, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
