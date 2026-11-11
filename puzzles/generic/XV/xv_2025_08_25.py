"""PuzzleMadness X/V Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
