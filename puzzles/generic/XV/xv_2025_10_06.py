"""PuzzleMadness X/V Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
