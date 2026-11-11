"""PuzzleMadness Anti-King Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 2, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 8, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 9, 0, 0, 7, 3, 0, 0],
        [4, 0, 0, 6, 0, 1, 0, 0, 7],
        [0, 7, 0, 9, 0, 0, 2, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 7, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
