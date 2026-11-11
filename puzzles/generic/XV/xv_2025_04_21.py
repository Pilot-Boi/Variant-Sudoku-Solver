"""PuzzleMadness X/V Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
