"""PuzzleMadness Anti-Knight Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 5, 7, 0, 0],
        [0, 5, 0, 0, 2, 8, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 3, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 5, 8, 0, 0, 0, 0, 4],
        [0, 2, 9, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
