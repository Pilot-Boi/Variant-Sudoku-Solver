"""PuzzleMadness Diagonal Sudoku — 2025-03-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 9, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 3, 0, 0, 0, 5, 0],
        [2, 0, 0, 8, 0, 0, 0, 0, 6],
        [0, 0, 4, 0, 0, 0, 6, 0, 1],
        [5, 0, 0, 0, 3, 0, 2, 9, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 3, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
