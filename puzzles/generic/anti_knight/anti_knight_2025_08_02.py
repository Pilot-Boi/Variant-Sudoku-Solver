"""PuzzleMadness Anti-Knight Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 5, 4, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 3, 7, 0],
        [0, 0, 0, 0, 7, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
