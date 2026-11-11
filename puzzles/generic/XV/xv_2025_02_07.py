"""PuzzleMadness X/V Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
