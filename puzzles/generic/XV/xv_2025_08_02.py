"""PuzzleMadness X/V Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
