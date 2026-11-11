"""PuzzleMadness Anti-King Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 5, 0, 0, 2, 3, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 9],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 8],
        [1, 0, 0, 0, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 8, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
