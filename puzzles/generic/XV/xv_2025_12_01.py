"""PuzzleMadness X/V Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'V')

    return puzzle
