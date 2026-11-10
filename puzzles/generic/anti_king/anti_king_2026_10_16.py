"""PuzzleMadness Anti-King Sudoku — 2026-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 7, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 4, 0, 0, 0, 0, 0, 5],
        [0, 0, 9, 0, 7, 4, 0, 0, 0],
        [0, 2, 0, 1, 0, 0, 0, 0, 0],
        [0, 4, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 2, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 6, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
