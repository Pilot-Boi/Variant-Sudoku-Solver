"""PuzzleMadness X/V Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
