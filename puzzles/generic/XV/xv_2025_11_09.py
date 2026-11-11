"""PuzzleMadness X/V Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
