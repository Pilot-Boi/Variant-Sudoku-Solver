"""PuzzleMadness X/V Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
