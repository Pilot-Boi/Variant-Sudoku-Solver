"""PuzzleMadness X/V Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
