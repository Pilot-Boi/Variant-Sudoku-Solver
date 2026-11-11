"""PuzzleMadness X/V Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
