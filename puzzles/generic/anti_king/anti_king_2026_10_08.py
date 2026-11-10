"""PuzzleMadness Anti-King Sudoku — 2026-10-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 9, 1, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 8, 0, 0, 0, 4, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 6, 0, 5, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
