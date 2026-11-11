"""PuzzleMadness Diagonal Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Diagonal Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/xsudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [3, 1, 0, 0, 0, 9, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 9, 6, 0, 7, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 3, 9, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_diagonal_constraints()

    return puzzle
