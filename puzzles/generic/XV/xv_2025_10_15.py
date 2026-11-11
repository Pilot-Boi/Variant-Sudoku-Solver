"""PuzzleMadness X/V Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')

    return puzzle
