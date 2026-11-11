"""PuzzleMadness X/V Sudoku — 2025-11-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
