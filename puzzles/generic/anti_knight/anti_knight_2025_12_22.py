"""PuzzleMadness Anti-Knight Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 4, 0, 0, 0, 0, 0, 0],
        [3, 0, 7, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 1, 3, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 8, 0, 0, 6, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
