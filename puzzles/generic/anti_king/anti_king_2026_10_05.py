"""PuzzleMadness Anti-King Sudoku — 2026-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 5],
        [0, 1, 7, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 1, 9, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 5, 2],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 9, 4, 0, 0, 0, 0, 0],
        [8, 6, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
