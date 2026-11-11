"""PuzzleMadness Anti-King Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 2, 4, 0, 0, 0],
        [9, 2, 0, 0, 3, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 9, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 8, 0, 0, 0, 0, 0, 1],
        [0, 6, 5, 0, 0, 0, 0, 3, 0],
        [0, 8, 0, 0, 5, 0, 0, 7, 0],
        [0, 0, 9, 0, 7, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
