"""PuzzleMadness X/V Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 2, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')

    return puzzle
