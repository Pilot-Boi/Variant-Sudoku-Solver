"""PuzzleMadness X/V Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')

    return puzzle
