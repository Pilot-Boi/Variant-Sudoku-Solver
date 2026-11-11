"""PuzzleMadness Diagonal Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 1, 0, 0, 0, 4],
        [8, 0, 0, 0, 0, 7, 2, 0, 0],
        [2, 0, 0, 9, 3, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 9, 0],
        [4, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
