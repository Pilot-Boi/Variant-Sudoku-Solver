"""PuzzleMadness X/V Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
