"""PuzzleMadness X/V Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
