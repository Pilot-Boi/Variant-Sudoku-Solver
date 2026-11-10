"""PuzzleMadness Anti-King Sudoku — 2026-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 8, 0, 0, 1, 0, 3, 0],
        [3, 0, 1, 9, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 2, 0, 6, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 8, 2, 7, 0, 1, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
