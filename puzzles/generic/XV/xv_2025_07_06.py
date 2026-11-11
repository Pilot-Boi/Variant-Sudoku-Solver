"""PuzzleMadness X/V Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
