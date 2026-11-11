"""PuzzleMadness Anti-King Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 5, 4, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 5],
        [0, 7, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 7, 0, 0, 0, 9],
        [6, 0, 3, 0, 8, 0, 0, 5, 0],
        [0, 0, 1, 0, 0, 0, 2, 6, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
