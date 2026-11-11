"""PuzzleMadness X/V Sudoku — 2025-06-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'V')

    return puzzle
