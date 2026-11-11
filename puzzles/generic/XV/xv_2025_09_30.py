"""PuzzleMadness X/V Sudoku — 2025-09-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
