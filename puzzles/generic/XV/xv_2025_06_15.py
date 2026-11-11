"""PuzzleMadness X/V Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')

    return puzzle
