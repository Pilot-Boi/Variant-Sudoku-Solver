"""PuzzleMadness Anti-King Sudoku — 2025-12-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-12-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/12/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 1, 6, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 1, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 0, 4, 3, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 8, 0, 3, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 8, 0, 0, 0, 3, 7, 0],
        [0, 0, 0, 0, 0, 0, 5, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
