"""PuzzleMadness X/V Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
