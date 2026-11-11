"""PuzzleMadness X/V Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
