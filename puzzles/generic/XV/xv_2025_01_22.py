"""PuzzleMadness X/V Sudoku — 2025-01-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
