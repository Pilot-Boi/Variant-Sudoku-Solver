"""PuzzleMadness X/V Sudoku — 2025-07-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
