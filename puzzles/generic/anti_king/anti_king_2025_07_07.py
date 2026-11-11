"""PuzzleMadness Anti-King Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [1, 0, 4, 0, 2, 0, 0, 0, 0],
        [5, 3, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 4, 6, 0, 1, 0, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 5],
        [0, 2, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
