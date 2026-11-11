"""PuzzleMadness Anti-King Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 2, 0, 3, 0, 0, 0],
        [0, 0, 0, 7, 9, 0, 0, 0, 3],
        [0, 0, 3, 0, 4, 0, 9, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 7, 0, 0, 0, 9],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 2, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 9, 2, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
