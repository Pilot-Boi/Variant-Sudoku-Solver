"""PuzzleMadness X/V Sudoku — 2025-07-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'V')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')

    return puzzle
