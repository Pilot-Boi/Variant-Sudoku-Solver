"""PuzzleMadness Anti-King Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 4, 0, 9, 8, 6, 0],
        [0, 0, 0, 0, 0, 2, 4, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 5, 8, 7, 3, 0, 0, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 6, 0, 0, 0, 0, 0, 0, 1],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
