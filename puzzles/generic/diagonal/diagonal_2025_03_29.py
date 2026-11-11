"""PuzzleMadness Diagonal Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 4, 0, 0, 0, 8, 0, 3, 0],
        [0, 5, 6, 2, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [2, 0, 7, 0, 6, 1, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
