"""PuzzleMadness X/V Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
