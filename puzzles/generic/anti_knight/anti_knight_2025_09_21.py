"""PuzzleMadness Anti-Knight Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 6, 0, 2, 7, 0, 0],
        [0, 9, 0, 7, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [2, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
