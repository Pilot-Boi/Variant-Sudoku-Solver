"""PuzzleMadness Anti-Knight Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 7, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 2, 3, 0, 5],
        [9, 4, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 2, 0, 1, 0, 0, 9],
        [2, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
