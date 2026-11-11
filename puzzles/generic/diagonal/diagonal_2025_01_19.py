"""PuzzleMadness Diagonal Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 9],
        [0, 2, 8, 9, 0, 0, 0, 0, 4],
        [7, 0, 0, 3, 0, 0, 8, 0, 0],
        [5, 1, 4, 2, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 8, 0, 0, 6, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
