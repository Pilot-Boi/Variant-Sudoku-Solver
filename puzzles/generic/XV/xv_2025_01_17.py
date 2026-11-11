"""PuzzleMadness X/V Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 8, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
