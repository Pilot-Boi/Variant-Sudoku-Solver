"""PuzzleMadness X/V Sudoku — 2025-01-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
