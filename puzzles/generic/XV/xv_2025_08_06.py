"""PuzzleMadness X/V Sudoku — 2025-08-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 8, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
