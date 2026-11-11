"""PuzzleMadness X/V Sudoku — 2025-11-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 3, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')

    return puzzle
