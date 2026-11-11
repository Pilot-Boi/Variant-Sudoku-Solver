"""PuzzleMadness Anti-Knight Sudoku — 2025-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 5, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 6, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 6, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
