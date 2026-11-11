"""PuzzleMadness X/V Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
