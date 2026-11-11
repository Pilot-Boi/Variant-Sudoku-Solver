"""PuzzleMadness Diagonal Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 5, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 3, 0, 0, 2, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 9, 0, 2, 0, 0, 1],
        [0, 4, 0, 0, 0, 1, 0, 0, 0],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
