"""PuzzleMadness Anti-Knight Sudoku — 2025-05-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-05-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/5/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 8, 0, 0, 0, 4, 0],
        [6, 0, 0, 1, 0, 0, 2, 7, 0],
        [0, 0, 0, 9, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 6, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
