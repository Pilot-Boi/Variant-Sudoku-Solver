"""PuzzleMadness X/V Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')

    return puzzle
