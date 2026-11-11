"""PuzzleMadness X/V Sudoku — 2025-02-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
