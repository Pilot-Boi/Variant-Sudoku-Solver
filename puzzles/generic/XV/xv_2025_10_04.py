"""PuzzleMadness X/V Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
