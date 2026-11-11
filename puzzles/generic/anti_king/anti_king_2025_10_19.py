"""PuzzleMadness Anti-King Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 8, 0, 5, 1, 0, 0],
        [0, 0, 3, 0, 1, 0, 8, 0, 0],
        [3, 0, 9, 0, 0, 0, 7, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 3],
        [1, 0, 6, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 9],
        [0, 0, 0, 0, 0, 2, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
