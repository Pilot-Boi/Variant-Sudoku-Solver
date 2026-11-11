"""PuzzleMadness X/V Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
