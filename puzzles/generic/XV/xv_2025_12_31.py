"""PuzzleMadness X/V Sudoku — 2025-12-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
