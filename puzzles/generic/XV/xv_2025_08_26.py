"""PuzzleMadness X/V Sudoku — 2025-08-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
