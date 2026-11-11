"""PuzzleMadness X/V Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 8, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
