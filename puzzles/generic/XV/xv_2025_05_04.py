"""PuzzleMadness X/V Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
