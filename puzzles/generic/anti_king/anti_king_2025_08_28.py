"""PuzzleMadness Anti-King Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 3, 0, 0],
        [0, 3, 9, 0, 0, 0, 4, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 5, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 1, 0, 0, 4, 8, 0, 0],
        [0, 5, 6, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 9, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
