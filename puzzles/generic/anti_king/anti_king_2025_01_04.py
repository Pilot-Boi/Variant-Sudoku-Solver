"""PuzzleMadness Anti-King Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 6],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 0, 0, 0, 0, 0, 2, 6, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [6, 1, 7, 0, 0, 0, 4, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
