"""PuzzleMadness Anti-Knight Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 8, 0, 0, 0, 6, 0, 0, 0],
        [0, 5, 0, 9, 0, 0, 0, 7, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 9, 3, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 3, 0, 0, 0, 2, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
