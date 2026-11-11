"""PuzzleMadness X/V Sudoku — 2025-01-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
