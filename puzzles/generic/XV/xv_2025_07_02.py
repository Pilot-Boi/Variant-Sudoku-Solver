"""PuzzleMadness X/V Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'V')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
