"""PuzzleMadness Diagonal Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 4, 0, 7, 3, 6],
        [8, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 5, 3, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 7, 2, 0, 0, 0, 0, 5],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
