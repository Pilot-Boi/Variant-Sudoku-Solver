"""PuzzleMadness Diagonal Sudoku — 2025-06-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-06-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/6/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 4, 7, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 0, 6, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 3],
        [0, 1, 4, 2, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
