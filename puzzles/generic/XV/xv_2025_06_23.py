"""PuzzleMadness X/V Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 8, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
