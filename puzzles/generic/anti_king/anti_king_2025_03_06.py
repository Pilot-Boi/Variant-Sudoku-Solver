"""PuzzleMadness Anti-King Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 0, 0, 0, 0, 4, 0],
        [0, 2, 0, 5, 0, 0, 6, 7, 0],
        [0, 0, 0, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [8, 0, 0, 0, 9, 4, 0, 0, 0],
        [0, 5, 0, 0, 6, 2, 0, 0, 3],
        [0, 1, 0, 0, 0, 5, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
