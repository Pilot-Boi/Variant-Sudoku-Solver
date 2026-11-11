"""PuzzleMadness Anti-King Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 2, 0, 0, 0, 0, 0, 3],
        [0, 8, 3, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 4, 0, 0, 2, 0, 0],
        [8, 0, 6, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 4, 0, 0, 6, 0, 0, 8],
        [0, 0, 0, 0, 0, 3, 5, 7, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
