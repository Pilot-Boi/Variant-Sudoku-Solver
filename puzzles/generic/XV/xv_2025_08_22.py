"""PuzzleMadness X/V Sudoku — 2025-08-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 1, 0, 0, 9],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
