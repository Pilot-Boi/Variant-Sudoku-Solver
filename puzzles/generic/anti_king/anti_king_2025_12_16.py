"""PuzzleMadness Anti-King Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 6, 7, 2],
        [0, 0, 0, 0, 4, 9, 0, 3, 0],
        [0, 0, 3, 8, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 7, 0, 2, 0, 5],
        [3, 0, 0, 0, 5, 0, 0, 9, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 8, 3],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
