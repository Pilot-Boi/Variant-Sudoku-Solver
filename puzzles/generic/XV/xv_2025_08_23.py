"""PuzzleMadness X/V Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
