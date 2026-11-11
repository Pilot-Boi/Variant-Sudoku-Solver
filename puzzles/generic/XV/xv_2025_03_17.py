"""PuzzleMadness X/V Sudoku — 2025-03-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
