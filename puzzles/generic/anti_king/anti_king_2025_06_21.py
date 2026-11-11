"""PuzzleMadness Anti-King Sudoku — 2025-06-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 9, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 9],
        [0, 0, 0, 0, 8, 7, 0, 0, 0],
        [6, 8, 0, 0, 1, 0, 0, 0, 0],
        [0, 3, 2, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 7, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
