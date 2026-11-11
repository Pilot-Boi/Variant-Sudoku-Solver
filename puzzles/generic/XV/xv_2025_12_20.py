"""PuzzleMadness X/V Sudoku — 2025-12-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
