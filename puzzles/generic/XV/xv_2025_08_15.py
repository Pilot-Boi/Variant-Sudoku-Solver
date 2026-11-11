"""PuzzleMadness X/V Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 1, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 2],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
