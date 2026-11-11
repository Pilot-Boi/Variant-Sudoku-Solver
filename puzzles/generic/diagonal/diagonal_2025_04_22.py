"""PuzzleMadness Diagonal Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 7, 2, 0, 9, 0, 0],
        [1, 5, 0, 0, 8, 6, 3, 0, 0],
        [7, 4, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 9, 0],
        [0, 9, 8, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 6, 0, 1, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
