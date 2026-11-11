"""PuzzleMadness X/V Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')

    return puzzle
