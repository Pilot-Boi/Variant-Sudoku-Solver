"""PuzzleMadness Anti-King Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 5, 0, 9, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [1, 0, 4, 3, 0, 7, 2, 0, 5],
        [8, 0, 7, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
