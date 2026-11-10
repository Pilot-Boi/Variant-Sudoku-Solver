"""PuzzleMadness Anti-Knight Sudoku — 2026-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2026-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2026/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
        [5, 6, 0, 0, 4, 0, 0, 0, 0],
        [8, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [7, 0, 0, 0, 9, 0, 5, 0, 0],
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
