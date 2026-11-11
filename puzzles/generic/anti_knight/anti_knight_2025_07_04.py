"""PuzzleMadness Anti-Knight Sudoku — 2025-07-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-07-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/7/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 5, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 4, 8, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 4, 0, 0, 0, 5, 0, 0],
        [0, 0, 1, 0, 2, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
