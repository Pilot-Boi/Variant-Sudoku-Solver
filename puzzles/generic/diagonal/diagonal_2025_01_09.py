"""PuzzleMadness Diagonal Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 3, 0, 0, 8, 6, 0, 9, 2],
        [4, 0, 0, 0, 3, 0, 9, 0, 1],
        [3, 1, 2, 0, 0, 0, 6, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
