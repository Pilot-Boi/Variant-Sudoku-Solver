"""PuzzleMadness Anti-King Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 5, 2, 8, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 0, 1, 9],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 4],
        [6, 9, 8, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 3, 0, 0, 0],
        [0, 8, 0, 4, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
