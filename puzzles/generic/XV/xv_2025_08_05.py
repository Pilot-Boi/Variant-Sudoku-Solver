"""PuzzleMadness X/V Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')

    return puzzle
