"""PuzzleMadness X/V Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
