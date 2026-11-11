"""PuzzleMadness Anti-Knight Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 4, 0, 0, 1],
        [9, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 2, 8, 0, 0, 3, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
