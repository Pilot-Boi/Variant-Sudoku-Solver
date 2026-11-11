"""PuzzleMadness X/V Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 2, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
