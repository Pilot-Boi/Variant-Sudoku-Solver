"""PuzzleMadness Anti-Knight Sudoku — 2025-06-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-06-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/6/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 4, 3, 0],
        [0, 0, 1, 0, 5, 8, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 0, 2, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
