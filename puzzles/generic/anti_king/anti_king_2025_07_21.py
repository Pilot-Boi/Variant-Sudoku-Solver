"""PuzzleMadness Anti-King Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 1, 2, 4, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 4, 7, 0, 2, 0, 1, 6],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 2],
        [0, 4, 0, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 1, 9, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
