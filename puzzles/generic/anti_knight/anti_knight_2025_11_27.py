"""PuzzleMadness Anti-Knight Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 3, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 5, 3, 0, 0, 0],
        [0, 9, 6, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 2, 6, 0, 0, 0],
        [0, 2, 3, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 3],
        [0, 0, 1, 0, 0, 0, 2, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
