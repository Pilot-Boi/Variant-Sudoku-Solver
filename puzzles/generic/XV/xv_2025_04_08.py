"""PuzzleMadness X/V Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
