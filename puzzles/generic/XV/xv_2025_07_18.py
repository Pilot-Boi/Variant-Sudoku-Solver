"""PuzzleMadness X/V Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
