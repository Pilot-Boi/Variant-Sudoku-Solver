"""PuzzleMadness Anti-King Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 9, 0],
        [0, 0, 0, 0, 6, 0, 0, 2, 1],
        [5, 0, 6, 0, 0, 0, 0, 0, 0],
        [3, 9, 0, 0, 0, 0, 0, 0, 4],
        [0, 8, 2, 0, 0, 0, 0, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 3, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
