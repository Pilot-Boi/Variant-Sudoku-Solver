"""PuzzleMadness Diagonal Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 8, 0, 0, 0, 9],
        [0, 0, 8, 0, 5, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 6, 0, 0, 0, 0],
        [4, 0, 0, 0, 2, 8, 0, 5, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [5, 0, 0, 3, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
