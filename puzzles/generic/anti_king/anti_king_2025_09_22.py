"""PuzzleMadness Anti-King Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [2, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 9, 0, 0, 6, 0, 0, 7],
        [0, 0, 0, 4, 0, 0, 0, 9, 6],
        [7, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 9, 5, 0, 6, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
