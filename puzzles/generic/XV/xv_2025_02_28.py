"""PuzzleMadness X/V Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')

    return puzzle
