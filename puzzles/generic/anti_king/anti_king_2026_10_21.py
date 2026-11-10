"""PuzzleMadness Anti-King Sudoku — 2026-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 8, 6, 0, 3, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 4],
        [3, 0, 0, 8, 0, 0, 0, 0, 1],
        [4, 0, 0, 7, 5, 0, 0, 0, 0],
        [9, 8, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 5, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
