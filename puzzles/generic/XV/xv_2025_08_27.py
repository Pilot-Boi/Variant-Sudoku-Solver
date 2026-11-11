"""PuzzleMadness X/V Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [5, 6, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
