"""PuzzleMadness Diagonal Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 5, 3, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 3, 0, 0, 0],
        [0, 0, 9, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 5, 2, 0, 6, 0, 0, 8],
        [0, 0, 0, 9, 6, 4, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [4, 9, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
