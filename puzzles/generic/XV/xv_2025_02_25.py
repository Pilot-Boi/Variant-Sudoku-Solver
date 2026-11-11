"""PuzzleMadness X/V Sudoku — 2025-02-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
