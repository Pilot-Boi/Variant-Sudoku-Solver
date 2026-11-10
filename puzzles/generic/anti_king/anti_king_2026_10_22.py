"""PuzzleMadness Anti-King Sudoku — 2026-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 9, 0, 3, 0, 0, 0, 1],
        [6, 0, 0, 0, 0, 1, 7, 0, 0],
        [0, 1, 0, 8, 0, 0, 0, 5, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [2, 0, 0, 0, 0, 0, 0, 9, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
