"""PuzzleMadness Anti-Knight Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 8, 0, 1, 6],
        [7, 6, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 2, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 4, 0],
        [0, 9, 0, 0, 0, 0, 0, 2, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
