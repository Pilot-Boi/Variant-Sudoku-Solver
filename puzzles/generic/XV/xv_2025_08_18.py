"""PuzzleMadness X/V Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
