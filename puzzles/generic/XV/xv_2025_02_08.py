"""PuzzleMadness X/V Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
