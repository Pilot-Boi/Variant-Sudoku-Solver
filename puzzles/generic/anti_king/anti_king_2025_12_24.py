"""PuzzleMadness Anti-King Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 1, 4, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [3, 0, 8, 1, 0, 0, 7, 0, 0],
        [0, 0, 9, 0, 0, 0, 2, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 3, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
