"""PuzzleMadness X/V Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
