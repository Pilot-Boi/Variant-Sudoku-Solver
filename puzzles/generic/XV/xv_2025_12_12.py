"""PuzzleMadness X/V Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')

    return puzzle
