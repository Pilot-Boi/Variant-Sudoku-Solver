"""PuzzleMadness X/V Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 4, 7, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')

    return puzzle
