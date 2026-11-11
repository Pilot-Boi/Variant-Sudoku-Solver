"""PuzzleMadness X/V Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
