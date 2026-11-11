"""PuzzleMadness Anti-King Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 2, 6, 0],
        [0, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 7, 5, 0, 0, 0, 0, 4, 3],
        [9, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 8, 0, 0, 9, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 7, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 7, 5, 1, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
