"""PuzzleMadness Anti-King Sudoku — 2025-05-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 9, 0, 0, 5, 6, 8, 2, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 5],
        [5, 0, 0, 0, 3, 0, 0, 6, 1],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 7, 9, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 7, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
