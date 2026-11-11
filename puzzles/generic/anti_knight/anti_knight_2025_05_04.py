"""PuzzleMadness Anti-Knight Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 0, 0, 0],
        [9, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 2, 4, 0, 0, 0, 6, 0, 0],
        [0, 0, 7, 3, 2, 0, 9, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 3, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
