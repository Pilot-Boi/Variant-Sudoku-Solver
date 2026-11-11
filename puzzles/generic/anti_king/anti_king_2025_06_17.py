"""PuzzleMadness Anti-King Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 8, 7, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 2, 8, 1, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 5, 1, 0, 4, 8, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
