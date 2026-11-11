"""PuzzleMadness Anti-King Sudoku — 2025-02-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-02-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/2/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 5, 0, 0, 7, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 3],
        [0, 0, 7, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [3, 2, 0, 0, 0, 0, 4, 5, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
