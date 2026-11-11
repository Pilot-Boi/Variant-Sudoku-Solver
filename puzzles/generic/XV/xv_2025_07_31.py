"""PuzzleMadness X/V Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
