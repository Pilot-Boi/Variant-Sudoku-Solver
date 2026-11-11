"""PuzzleMadness X/V Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 5, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
