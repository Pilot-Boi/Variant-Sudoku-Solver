"""PuzzleMadness Anti-King Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 2, 3, 8, 0, 4, 0, 9],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 5, 4, 2],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 8, 4, 9, 7, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 1, 8],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
