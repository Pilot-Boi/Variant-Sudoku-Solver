"""PuzzleMadness X/V Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')

    return puzzle
