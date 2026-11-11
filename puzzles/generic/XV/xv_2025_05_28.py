"""PuzzleMadness X/V Sudoku — 2025-05-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')

    return puzzle
