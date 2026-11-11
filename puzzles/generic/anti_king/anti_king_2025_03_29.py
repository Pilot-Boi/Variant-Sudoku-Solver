"""PuzzleMadness Anti-King Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-King Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/antikingsudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 9, 6, 0],
        [0, 0, 0, 0, 4, 0, 0, 5, 0],
        [9, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 3, 5, 0, 0, 0, 0, 9],
        [3, 0, 2, 0, 0, 0, 0, 0, 0],
        [1, 9, 0, 8, 0, 3, 2, 0, 4],
        [4, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_king_constraints()

    return puzzle
