"""PuzzleMadness Diagonal Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 4, 0, 6, 8, 0],
        [0, 0, 3, 0, 0, 8, 0, 9, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 8, 0, 0, 0, 1, 3, 6, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 7, 0, 2, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
