"""PuzzleMadness X/V Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
