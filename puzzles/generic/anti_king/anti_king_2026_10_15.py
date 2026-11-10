"""PuzzleMadness Anti-King Sudoku — 2026-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 4, 0, 0],
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
        [3, 0, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 8, 7, 0, 0, 0, 0, 0],
        [5, 3, 0, 6, 4, 0, 0, 0, 0],
        [0, 0, 4, 0, 5, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
