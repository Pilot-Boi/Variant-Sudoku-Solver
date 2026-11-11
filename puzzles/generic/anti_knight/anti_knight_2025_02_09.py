"""PuzzleMadness Anti-Knight Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 7, 0, 0, 1, 0, 0],
        [5, 6, 1, 0, 0, 0, 8, 4, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 5, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 3, 0],
        [0, 0, 0, 1, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
