"""PuzzleMadness X/V Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
