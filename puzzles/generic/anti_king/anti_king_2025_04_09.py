"""PuzzleMadness Anti-King Sudoku — 2025-04-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-04-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/4/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 9, 4, 0, 0, 0, 2],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 7, 0],
        [0, 0, 0, 3, 0, 4, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [4, 0, 0, 1, 0, 0, 0, 0, 9],
        [7, 3, 0, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 8, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
