"""PuzzleMadness X/V Sudoku — 2025-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')

    return puzzle
