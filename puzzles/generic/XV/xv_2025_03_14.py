"""PuzzleMadness X/V Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 8, 6, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
