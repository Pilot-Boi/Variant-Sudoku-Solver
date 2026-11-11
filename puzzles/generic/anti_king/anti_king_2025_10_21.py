"""PuzzleMadness Anti-King Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 4, 0, 0, 8, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 6, 1, 0, 5, 0, 0, 0],
        [0, 7, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 3, 5, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 1, 0, 5, 0, 9, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
