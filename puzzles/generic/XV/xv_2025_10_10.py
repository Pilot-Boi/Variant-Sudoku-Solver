"""PuzzleMadness X/V Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
