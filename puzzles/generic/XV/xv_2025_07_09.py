"""PuzzleMadness X/V Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
