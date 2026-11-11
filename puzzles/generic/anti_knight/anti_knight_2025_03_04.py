"""PuzzleMadness Anti-Knight Sudoku — 2025-03-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-03-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/3/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 7, 9, 5, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
