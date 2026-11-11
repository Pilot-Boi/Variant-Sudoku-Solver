"""PuzzleMadness Anti-King Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 9, 0, 3, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 5],
        [5, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [1, 0, 7, 0, 0, 9, 5, 8, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
