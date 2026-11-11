"""PuzzleMadness Anti-King Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 9, 2, 0, 0, 6, 0],
        [0, 0, 0, 0, 3, 4, 5, 0, 9],
        [0, 0, 0, 6, 0, 0, 0, 0, 8],
        [6, 8, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 8, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 7, 0, 1],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
