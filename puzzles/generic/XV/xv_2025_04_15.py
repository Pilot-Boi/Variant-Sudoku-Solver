"""PuzzleMadness X/V Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
