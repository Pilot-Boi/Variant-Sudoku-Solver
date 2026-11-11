"""PuzzleMadness X/V Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
