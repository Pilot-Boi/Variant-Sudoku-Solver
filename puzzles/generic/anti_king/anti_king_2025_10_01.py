"""PuzzleMadness Anti-King Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 7, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 8, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 1],
        [8, 0, 1, 0, 0, 7, 0, 2, 0],
        [2, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 3, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
