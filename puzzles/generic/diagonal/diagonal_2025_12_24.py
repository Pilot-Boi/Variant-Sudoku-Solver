"""PuzzleMadness Diagonal Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 4],
        [0, 6, 0, 0, 0, 8, 3, 0, 1],
        [0, 0, 0, 0, 7, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 4, 6, 0, 1, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 5, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
