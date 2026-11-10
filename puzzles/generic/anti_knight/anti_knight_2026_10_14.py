"""PuzzleMadness Anti-Knight Sudoku — 2026-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2026-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2026/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 8, 4, 7],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 9, 0],
        [0, 0, 0, 0, 0, 0, 2, 8, 0],
        [0, 9, 6, 0, 0, 0, 4, 0, 0],
        [5, 0, 8, 0, 0, 4, 0, 0, 0],
        [7, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
