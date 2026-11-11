"""PuzzleMadness X/V Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')

    return puzzle
