"""PuzzleMadness X/V Sudoku — 2025-01-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
