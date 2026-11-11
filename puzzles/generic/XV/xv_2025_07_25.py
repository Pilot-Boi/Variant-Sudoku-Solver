"""PuzzleMadness X/V Sudoku — 2025-07-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 5, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
