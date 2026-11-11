"""PuzzleMadness Anti-King Sudoku — 2025-04-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-04-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/4/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 5, 0, 7, 3, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 6, 4, 3, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 9, 0, 3, 0],
        [6, 3, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 6],
        [0, 8, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 9, 0, 0, 8, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
