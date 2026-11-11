"""PuzzleMadness X/V Sudoku — 2025-01-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
