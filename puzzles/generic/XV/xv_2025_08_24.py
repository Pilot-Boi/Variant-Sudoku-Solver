"""PuzzleMadness X/V Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
