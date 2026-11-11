"""PuzzleMadness Anti-King Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 5, 8, 0, 0, 0, 0, 2],
        [0, 2, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 5, 0],
        [0, 0, 0, 9, 0, 0, 0, 4, 1],
        [5, 0, 2, 7, 6, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 2, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
