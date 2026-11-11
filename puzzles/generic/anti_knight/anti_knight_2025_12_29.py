"""PuzzleMadness Anti-Knight Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 9, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 4, 8, 0, 6, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
