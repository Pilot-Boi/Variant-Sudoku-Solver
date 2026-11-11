"""PuzzleMadness Diagonal Sudoku — 2025-03-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 2, 0, 0],
        [4, 0, 0, 0, 0, 2, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 4],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 6],
        [7, 0, 2, 0, 0, 0, 0, 3, 1],
        [0, 0, 8, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 3, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
