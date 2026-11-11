"""PuzzleMadness X/V Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 7, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')

    return puzzle
