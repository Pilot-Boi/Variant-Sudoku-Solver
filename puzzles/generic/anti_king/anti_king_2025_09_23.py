"""PuzzleMadness Anti-King Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 4, 0, 7, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [6, 0, 0, 0, 5, 0, 3, 0, 0],
        [0, 8, 5, 0, 0, 0, 0, 0, 2],
        [0, 6, 0, 0, 0, 5, 2, 0, 0],
        [0, 0, 0, 3, 0, 9, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
