"""PuzzleMadness Anti-Knight Sudoku — 2025-07-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-07-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/7/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 7, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 1, 4, 0, 6, 0],
        [5, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 5, 3, 0],
        [0, 0, 0, 0, 0, 7, 4, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
