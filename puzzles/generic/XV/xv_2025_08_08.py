"""PuzzleMadness X/V Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
