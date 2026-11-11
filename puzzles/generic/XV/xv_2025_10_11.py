"""PuzzleMadness X/V Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
