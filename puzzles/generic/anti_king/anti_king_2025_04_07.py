"""PuzzleMadness Anti-King Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 7, 4, 9, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 2, 0, 3, 0, 4, 0],
        [1, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
