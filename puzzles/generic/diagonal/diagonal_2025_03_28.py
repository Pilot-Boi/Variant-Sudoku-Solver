"""PuzzleMadness Diagonal Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 6, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
        [0, 5, 8, 0, 0, 0, 0, 0, 6],
        [0, 0, 6, 8, 0, 0, 9, 1, 0],
        [5, 0, 0, 3, 0, 0, 0, 4, 9],
        [0, 3, 7, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
