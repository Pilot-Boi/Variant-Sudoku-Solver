"""PuzzleMadness X/V Sudoku — 2025-09-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')

    return puzzle
