"""PuzzleMadness Anti-King Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 6, 0, 0, 2],
        [0, 0, 0, 0, 8, 4, 0, 0, 7],
        [5, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 2, 0, 7, 6, 0, 0],
        [0, 0, 4, 8, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 1],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
