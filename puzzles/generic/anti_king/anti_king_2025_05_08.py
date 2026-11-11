"""PuzzleMadness Anti-King Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 5, 0, 0, 0, 3, 0],
        [7, 6, 8, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 6, 0, 3, 2, 0, 0, 0],
        [0, 1, 3, 4, 7, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
