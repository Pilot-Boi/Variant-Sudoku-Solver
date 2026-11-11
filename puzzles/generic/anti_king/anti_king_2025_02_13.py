"""PuzzleMadness Anti-King Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [6, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 9, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 7, 0, 0, 5, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 3, 6, 0, 0],
        [9, 0, 0, 0, 0, 0, 4, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
