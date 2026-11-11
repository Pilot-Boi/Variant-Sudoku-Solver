"""PuzzleMadness Anti-Knight Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 1, 0, 7, 0, 0, 0, 0],
        [0, 6, 0, 5, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 1, 4, 0],
        [0, 0, 7, 1, 6, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
