"""PuzzleMadness Standard Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Standard Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 7, 0, 0, 0, 6],
        [7, 0, 6, 8, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 2, 4, 3],
        [0, 0, 0, 0, 8, 0, 7, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 6, 0],
        [0, 7, 0, 0, 0, 1, 0, 0, 0],
        [4, 8, 5, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)



    return puzzle
