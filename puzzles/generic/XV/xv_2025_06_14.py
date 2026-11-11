"""PuzzleMadness X/V Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 4, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')

    return puzzle
