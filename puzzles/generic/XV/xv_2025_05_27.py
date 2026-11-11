"""PuzzleMadness X/V Sudoku — 2025-05-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
