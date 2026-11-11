"""PuzzleMadness Anti-Knight Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 8],
        [0, 0, 3, 7, 0, 0, 0, 0, 1],
        [0, 4, 0, 0, 9, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 1, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
        [0, 1, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
