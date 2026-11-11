"""PuzzleMadness Diagonal Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 4, 8, 3],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 2, 0, 4],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 8],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 4, 3, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
