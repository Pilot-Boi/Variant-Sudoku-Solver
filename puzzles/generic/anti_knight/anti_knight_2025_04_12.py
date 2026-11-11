"""PuzzleMadness Anti-Knight Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 6, 0, 0, 3, 5, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 4, 0, 9, 0, 0, 3, 5],
        [5, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
