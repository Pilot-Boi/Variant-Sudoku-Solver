"""PuzzleMadness X/V Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
