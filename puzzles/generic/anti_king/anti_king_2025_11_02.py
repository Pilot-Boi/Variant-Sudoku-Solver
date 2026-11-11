"""PuzzleMadness Anti-King Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0, 5],
        [5, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 4, 6, 0, 2, 0, 0, 7, 0],
        [0, 0, 0, 0, 1, 8, 3, 0, 0],
        [0, 7, 0, 0, 0, 0, 5, 1, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
