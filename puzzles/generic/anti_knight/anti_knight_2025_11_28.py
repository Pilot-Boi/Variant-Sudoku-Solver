"""PuzzleMadness Anti-Knight Sudoku — 2025-11-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-11-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/11/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 5, 4, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 4, 0, 5, 0, 0],
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
