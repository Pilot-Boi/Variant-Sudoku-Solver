"""PuzzleMadness Diagonal Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 4, 0, 3, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 2, 0],
        [0, 0, 0, 5, 3, 0, 0, 0, 0],
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 2],
        [0, 0, 0, 3, 6, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 8, 1, 0, 4],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
