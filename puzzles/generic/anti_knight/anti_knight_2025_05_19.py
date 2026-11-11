"""PuzzleMadness Anti-Knight Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/5/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 8, 0, 7, 0, 0, 0],
        [0, 6, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 0, 7],
        [4, 5, 0, 6, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 5, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
