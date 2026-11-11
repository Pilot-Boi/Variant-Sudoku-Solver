"""PuzzleMadness X/V Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
