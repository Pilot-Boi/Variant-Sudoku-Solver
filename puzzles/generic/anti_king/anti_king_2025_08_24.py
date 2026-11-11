"""PuzzleMadness Anti-King Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 9],
        [0, 0, 9, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 6, 0, 1, 0, 0, 4],
        [0, 2, 8, 0, 0, 0, 5, 0, 0],
        [4, 9, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 5, 1, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 8, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
