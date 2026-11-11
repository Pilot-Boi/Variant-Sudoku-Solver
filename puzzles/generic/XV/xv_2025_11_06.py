"""PuzzleMadness X/V Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
