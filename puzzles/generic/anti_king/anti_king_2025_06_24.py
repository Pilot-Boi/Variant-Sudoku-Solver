"""PuzzleMadness Anti-King Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 8, 7, 0, 0, 3],
        [0, 3, 0, 0, 0, 6, 0, 0, 0],
        [0, 7, 0, 3, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 0, 9, 0, 3, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 8],
        [8, 0, 0, 0, 0, 0, 4, 0, 0],
        [5, 9, 0, 8, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
