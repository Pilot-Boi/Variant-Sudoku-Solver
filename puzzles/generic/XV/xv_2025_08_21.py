"""PuzzleMadness X/V Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
