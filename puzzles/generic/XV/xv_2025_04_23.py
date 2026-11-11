"""PuzzleMadness X/V Sudoku — 2025-04-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
