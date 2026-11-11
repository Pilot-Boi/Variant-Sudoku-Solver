"""PuzzleMadness X/V Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
