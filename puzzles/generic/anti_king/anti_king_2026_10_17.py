"""PuzzleMadness Anti-King Sudoku — 2026-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 5, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 0],
        [0, 7, 2, 4, 9, 5, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 4, 0, 3],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 7, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
