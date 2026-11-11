"""PuzzleMadness X/V Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
