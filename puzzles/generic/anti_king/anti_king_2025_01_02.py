"""PuzzleMadness Anti-King Sudoku — 2025-01-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 2, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 2, 9, 0, 0],
        [0, 0, 5, 0, 7, 0, 0, 0, 0],
        [0, 6, 0, 9, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 0, 0, 1, 8, 0],
        [9, 0, 1, 5, 0, 0, 0, 2, 0],
        [3, 0, 6, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
