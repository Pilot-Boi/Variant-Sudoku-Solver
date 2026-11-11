"""PuzzleMadness X/V Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 7],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
