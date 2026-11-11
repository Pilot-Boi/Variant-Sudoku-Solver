"""PuzzleMadness X/V Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
