"""PuzzleMadness Anti-King Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 6, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 4, 9, 7, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 0, 0, 7, 0, 8, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [7, 2, 0, 0, 6, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 3, 0, 6],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [6, 0, 0, 0, 1, 0, 7, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
