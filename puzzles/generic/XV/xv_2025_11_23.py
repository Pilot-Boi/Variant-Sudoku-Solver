"""PuzzleMadness X/V Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
