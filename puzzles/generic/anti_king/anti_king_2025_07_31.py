"""PuzzleMadness Anti-King Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 1, 0, 0, 2, 0, 0],
        [0, 1, 0, 4, 0, 9, 0, 0, 0],
        [0, 3, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 8],
        [0, 0, 0, 0, 0, 4, 3, 0, 6],
        [5, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
