"""PuzzleMadness X/V Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'V')

    return puzzle
