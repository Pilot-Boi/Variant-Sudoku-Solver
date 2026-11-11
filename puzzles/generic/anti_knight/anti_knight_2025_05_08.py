"""PuzzleMadness Anti-Knight Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 3, 0, 0, 0, 0],
        [0, 7, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 7],
        [7, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 6, 0, 0, 4],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
