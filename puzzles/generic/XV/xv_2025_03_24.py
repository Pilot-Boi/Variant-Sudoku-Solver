"""PuzzleMadness X/V Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'V')

    return puzzle
