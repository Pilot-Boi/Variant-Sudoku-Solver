"""PuzzleMadness Anti-King Sudoku — 2026-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 5, 9],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 8, 0, 5, 0, 9, 0],
        [0, 4, 5, 3, 0, 7, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 1, 0, 0, 0, 8, 3],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
