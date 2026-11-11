"""PuzzleMadness Anti-Knight Sudoku — 2025-10-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-10-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/10/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 1, 0, 0, 7, 3],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 3, 0, 5],
        [0, 9, 6, 0, 0, 2, 8, 1, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 7, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
