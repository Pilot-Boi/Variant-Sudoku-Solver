"""PuzzleMadness Anti-King Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 7, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 3, 2, 9, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 5, 0, 9, 0],
        [7, 6, 0, 1, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
