"""PuzzleMadness X/V Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 5, 0, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')

    return puzzle
