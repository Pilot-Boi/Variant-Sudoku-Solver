"""PuzzleMadness X/V Sudoku — 2025-07-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
