"""PuzzleMadness Anti-Knight Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 3, 8, 0],
        [0, 0, 0, 6, 4, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
