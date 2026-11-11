"""PuzzleMadness X/V Sudoku — 2025-07-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
