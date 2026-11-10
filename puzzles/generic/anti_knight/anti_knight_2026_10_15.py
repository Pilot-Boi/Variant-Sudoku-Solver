"""PuzzleMadness Anti-Knight Sudoku — 2026-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2026-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2026/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 7, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 4, 0, 0, 8, 0, 1],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
