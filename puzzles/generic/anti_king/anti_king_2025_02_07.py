"""PuzzleMadness Anti-King Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [4, 9, 6, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 3, 0, 1, 0, 0, 0],
        [2, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 5, 0, 0, 1, 9, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
