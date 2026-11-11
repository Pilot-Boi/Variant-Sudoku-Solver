"""PuzzleMadness Diagonal Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [5, 0, 7, 0, 3, 0, 1, 0, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 3],
        [7, 8, 0, 6, 5, 2, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
