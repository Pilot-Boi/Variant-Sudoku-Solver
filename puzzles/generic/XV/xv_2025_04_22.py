"""PuzzleMadness X/V Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'V')

    return puzzle
