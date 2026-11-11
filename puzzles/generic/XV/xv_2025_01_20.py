"""PuzzleMadness X/V Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
