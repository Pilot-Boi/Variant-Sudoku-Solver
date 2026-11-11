"""PuzzleMadness X/V Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
