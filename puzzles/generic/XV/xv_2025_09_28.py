"""PuzzleMadness X/V Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
