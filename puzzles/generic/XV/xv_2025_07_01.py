"""PuzzleMadness X/V Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
