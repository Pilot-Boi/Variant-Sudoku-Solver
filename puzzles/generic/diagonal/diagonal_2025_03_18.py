"""PuzzleMadness Diagonal Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 2, 0, 5, 0],
        [0, 6, 2, 3, 0, 1, 0, 0, 5],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [3, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
