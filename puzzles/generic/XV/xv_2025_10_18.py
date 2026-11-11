"""PuzzleMadness X/V Sudoku — 2025-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'V')

    return puzzle
