"""PuzzleMadness Anti-King Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 1, 2, 7, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 8, 1, 6, 0],
        [4, 0, 0, 0, 9, 0, 0, 8, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
