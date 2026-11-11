"""PuzzleMadness Anti-King Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 1, 0, 0, 3, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 7, 0, 0, 2],
        [3, 0, 2, 9, 0, 0, 0, 0, 1],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [2, 0, 9, 7, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 3, 0, 1, 0],
        [0, 0, 0, 8, 0, 6, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
