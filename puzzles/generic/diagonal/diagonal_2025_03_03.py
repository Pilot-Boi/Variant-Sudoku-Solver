"""PuzzleMadness Diagonal Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 8, 0, 0, 3, 0, 9, 0],
        [0, 0, 0, 4, 0, 0, 2, 6, 0],
        [9, 0, 0, 3, 0, 6, 0, 0, 0],
        [0, 3, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 2, 0],
        [0, 0, 1, 0, 0, 5, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
