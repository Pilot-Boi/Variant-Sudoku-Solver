"""PuzzleMadness Anti-Knight Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 1, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 2, 0],
        [7, 9, 5, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 2, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
