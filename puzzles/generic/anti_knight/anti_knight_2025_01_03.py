"""PuzzleMadness Anti-Knight Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 6, 3],
        [0, 0, 0, 0, 0, 3, 0, 5, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 5, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 6, 0, 7, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
