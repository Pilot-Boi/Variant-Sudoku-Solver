"""PuzzleMadness Anti-King Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 4, 3, 5, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 2, 9],
        [0, 7, 9, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
        [8, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [0, 0, 6, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
