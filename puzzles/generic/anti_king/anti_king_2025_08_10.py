"""PuzzleMadness Anti-King Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 5, 8, 0, 7, 0, 1, 0, 4],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [9, 0, 2, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 3, 0, 9],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 4, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
