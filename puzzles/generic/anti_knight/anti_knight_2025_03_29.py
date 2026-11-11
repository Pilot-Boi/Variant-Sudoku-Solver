"""PuzzleMadness Anti-Knight Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Anti-Knight Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/antiknightsudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 2, 8, 9, 0, 0, 7, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 9, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 8, 4, 3, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 7, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_anti_knight_constraints()

    return puzzle
