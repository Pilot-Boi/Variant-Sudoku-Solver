"""PuzzleMadness X/V Sudoku — 2025-12-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
