"""PuzzleMadness Anti-King Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 5, 0, 0, 0, 0, 1, 4, 0],
        [0, 4, 8, 0, 0, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 5, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 9, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
