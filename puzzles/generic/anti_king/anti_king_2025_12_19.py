"""PuzzleMadness Anti-King Sudoku — 2025-12-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-12-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/12/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 1, 0, 2, 0, 0, 0],
        [0, 0, 0, 8, 7, 0, 5, 2, 0],
        [0, 0, 1, 6, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 6, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 2, 6, 5, 0, 0, 0],
        [0, 0, 0, 4, 0, 9, 1, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
