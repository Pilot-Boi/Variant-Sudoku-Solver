"""PuzzleMadness Anti-King Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 4, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 0, 0, 5],
        [0, 5, 4, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 6, 0, 3, 5, 0, 9],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
