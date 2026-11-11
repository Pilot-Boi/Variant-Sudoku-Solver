"""PuzzleMadness Anti-King Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 5, 0, 0, 8, 0, 0, 0, 6],
        [0, 0, 0, 0, 4, 2, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 1, 0, 2, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 2, 5, 0, 3, 0],
        [7, 0, 0, 0, 3, 6, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
