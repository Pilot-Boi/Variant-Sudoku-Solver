"""PuzzleMadness Anti-King Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 6, 2, 0, 1],
        [0, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 8, 0, 0, 7, 0, 0, 9, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 3, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 6, 0, 8, 5, 0, 0],
        [4, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
