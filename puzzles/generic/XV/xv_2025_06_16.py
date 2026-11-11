"""PuzzleMadness X/V Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'V')

    return puzzle
