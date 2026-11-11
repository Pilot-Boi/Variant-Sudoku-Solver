"""PuzzleMadness Diagonal Sudoku — 2025-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 4, 8],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 4],
        [0, 4, 0, 0, 0, 0, 8, 6, 3],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 1, 3, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
