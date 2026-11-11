"""PuzzleMadness Anti-King Sudoku — 2025-09-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 9, 0],
        [5, 2, 7, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 1, 0, 2, 0, 0],
        [0, 3, 0, 2, 0, 0, 4, 6, 1],
        [0, 0, 0, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
