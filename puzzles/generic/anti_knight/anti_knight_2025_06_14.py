"""PuzzleMadness Anti-Knight Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 5, 7],
        [0, 0, 0, 0, 0, 0, 9, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 9, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [9, 0, 6, 0, 0, 0, 3, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
