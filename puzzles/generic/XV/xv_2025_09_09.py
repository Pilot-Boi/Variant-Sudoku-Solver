"""PuzzleMadness X/V Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
