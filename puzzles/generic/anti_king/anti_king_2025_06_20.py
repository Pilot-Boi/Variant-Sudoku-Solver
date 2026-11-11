"""PuzzleMadness Anti-King Sudoku — 2025-06-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 5, 0, 0, 6, 0, 9],
        [5, 0, 4, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 5, 7],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 4, 0, 0, 0, 8],
        [3, 5, 0, 6, 0, 0, 0, 7, 4],
        [0, 0, 0, 1, 0, 0, 5, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
