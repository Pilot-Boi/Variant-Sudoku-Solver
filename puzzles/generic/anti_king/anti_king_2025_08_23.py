"""PuzzleMadness Anti-King Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 0, 5],
        [5, 0, 0, 0, 2, 0, 8, 0, 4],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 5, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 8, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 6, 9, 0, 0, 0, 0, 0],
        [0, 1, 7, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
