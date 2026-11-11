"""PuzzleMadness X/V Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')

    return puzzle
