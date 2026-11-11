"""PuzzleMadness X/V Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
