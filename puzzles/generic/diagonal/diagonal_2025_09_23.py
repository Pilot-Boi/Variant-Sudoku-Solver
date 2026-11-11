"""PuzzleMadness Diagonal Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 1],
        [2, 0, 0, 0, 3, 0, 0, 0, 0],
        [8, 0, 1, 0, 0, 0, 0, 0, 9],
        [0, 5, 7, 0, 0, 0, 0, 0, 0],
        [4, 0, 9, 0, 0, 7, 3, 0, 0],
        [0, 0, 0, 7, 4, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
