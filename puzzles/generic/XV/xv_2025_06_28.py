"""PuzzleMadness X/V Sudoku — 2025-06-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')

    return puzzle
