"""PuzzleMadness Diagonal Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 4, 1, 2, 0],
        [0, 0, 2, 0, 7, 0, 0, 0, 0],
        [0, 4, 6, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 5, 0, 9],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 9, 0, 6],
        [0, 0, 3, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
