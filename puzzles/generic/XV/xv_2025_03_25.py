"""PuzzleMadness X/V Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
