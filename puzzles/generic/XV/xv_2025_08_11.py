"""PuzzleMadness X/V Sudoku — 2025-08-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')

    return puzzle
