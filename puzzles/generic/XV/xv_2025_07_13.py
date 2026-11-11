"""PuzzleMadness X/V Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
