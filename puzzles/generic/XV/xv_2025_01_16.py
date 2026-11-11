"""PuzzleMadness X/V Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 3],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 2, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 1), (0, 2), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
