"""PuzzleMadness X/V Sudoku — 2025-02-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 6), (3, 7), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'V')

    return puzzle
