"""PuzzleMadness Anti-King Sudoku — 2025-07-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 5, 0, 0, 1],
        [0, 0, 3, 8, 9, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 2, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 4, 0, 0, 0, 7, 0, 5],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 9, 0, 2, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
