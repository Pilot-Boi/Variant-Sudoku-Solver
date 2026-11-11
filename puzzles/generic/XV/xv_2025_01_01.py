"""PuzzleMadness X/V Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 2, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')

    return puzzle
