"""PuzzleMadness Anti-King Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 9, 0],
        [0, 0, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 7, 0, 0, 2, 6, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 4],
        [0, 0, 6, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 4, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
