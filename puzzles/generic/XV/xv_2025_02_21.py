"""PuzzleMadness X/V Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')

    return puzzle
