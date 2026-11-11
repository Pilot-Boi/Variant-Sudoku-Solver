"""PuzzleMadness X/V Sudoku — 2025-12-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')

    return puzzle
