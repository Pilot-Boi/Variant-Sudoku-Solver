"""PuzzleMadness X/V Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'V')
    puzzle.add_xv((6, 0), (7, 0), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
