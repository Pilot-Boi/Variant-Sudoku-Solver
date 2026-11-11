"""PuzzleMadness Anti-King Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 5, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 4, 7, 0, 0, 0, 0, 0],
        [0, 7, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 6, 2, 0, 0, 0, 4, 0],
        [1, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 1, 3, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 9, 0, 0, 0, 6, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
