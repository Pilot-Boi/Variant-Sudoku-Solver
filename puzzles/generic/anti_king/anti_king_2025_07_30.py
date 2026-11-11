"""PuzzleMadness Anti-King Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 5],
        [4, 0, 1, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 0, 2, 0, 0, 0, 9],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 1, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 8, 6, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
