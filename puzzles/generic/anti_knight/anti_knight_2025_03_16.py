"""PuzzleMadness Anti-Knight Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 8, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 8, 5, 0],
        [0, 0, 0, 0, 1, 4, 2, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
