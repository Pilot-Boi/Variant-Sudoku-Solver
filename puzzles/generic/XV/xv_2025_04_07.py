"""PuzzleMadness X/V Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 9, 0, 3, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
