"""PuzzleMadness X/V Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
