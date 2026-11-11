"""PuzzleMadness X/V Sudoku — 2025-07-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
