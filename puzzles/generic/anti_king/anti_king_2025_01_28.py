"""PuzzleMadness Anti-King Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 3, 0, 9, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 6, 7, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 0, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [3, 0, 0, 6, 0, 0, 2, 5, 7],
        [0, 0, 1, 5, 0, 4, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
