"""PuzzleMadness Diagonal Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 3, 4, 0, 0, 0, 0],
        [0, 3, 0, 1, 6, 2, 0, 0, 0],
        [0, 7, 0, 8, 0, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 8, 6, 0, 0, 0, 4, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
