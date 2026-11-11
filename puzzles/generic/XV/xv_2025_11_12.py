"""PuzzleMadness X/V Sudoku — 2025-11-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
