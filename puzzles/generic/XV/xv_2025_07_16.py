"""PuzzleMadness X/V Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 8, 0, 0, 7, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')

    return puzzle
