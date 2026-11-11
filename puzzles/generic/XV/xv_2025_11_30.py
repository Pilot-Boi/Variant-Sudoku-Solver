"""PuzzleMadness X/V Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
