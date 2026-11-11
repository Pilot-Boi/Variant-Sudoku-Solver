"""PuzzleMadness Anti-Knight Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 9, 0],
        [0, 4, 0, 1, 5, 0, 0, 6, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 6, 2, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
