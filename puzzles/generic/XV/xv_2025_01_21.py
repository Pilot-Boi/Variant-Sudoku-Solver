"""PuzzleMadness X/V Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
