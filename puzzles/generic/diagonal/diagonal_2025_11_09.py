"""PuzzleMadness Diagonal Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 8],
        [0, 0, 0, 7, 0, 5, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 3, 2, 8, 9, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 3, 7, 0, 6, 0, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
