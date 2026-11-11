"""PuzzleMadness Anti-King Sudoku — 2025-08-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 1, 0, 0, 0],
        [0, 5, 2, 0, 0, 0, 9, 0, 8],
        [0, 0, 0, 0, 2, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 1, 8, 0, 7, 0, 9, 0],
        [0, 0, 4, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
