"""PuzzleMadness Anti-King Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 3, 2, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 7, 3],
        [0, 3, 0, 0, 0, 0, 0, 5, 0],
        [6, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 1, 0, 0, 3, 0],
        [1, 0, 0, 0, 4, 0, 5, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
