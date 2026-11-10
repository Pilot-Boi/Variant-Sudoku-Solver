"""PuzzleMadness Anti-King Sudoku — 2026-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2026-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2026/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 4, 1, 0, 0, 0],
        [0, 7, 6, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 7, 2, 0, 0, 0],
        [0, 8, 4, 0, 0, 0, 0, 1, 0],
        [0, 3, 0, 6, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
