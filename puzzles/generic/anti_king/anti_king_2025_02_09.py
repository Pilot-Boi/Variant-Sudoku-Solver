"""PuzzleMadness Anti-King Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 2, 0],
        [2, 0, 3, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 6, 4, 5],
        [0, 0, 0, 0, 0, 8, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 6, 5, 0, 7],
        [0, 0, 0, 0, 7, 0, 2, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
