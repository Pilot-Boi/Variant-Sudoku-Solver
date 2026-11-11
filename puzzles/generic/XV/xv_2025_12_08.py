"""PuzzleMadness X/V Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
