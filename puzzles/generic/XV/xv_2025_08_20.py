"""PuzzleMadness X/V Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 7],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 5), (0, 6), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')

    return puzzle
