"""PuzzleMadness X/V Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 8],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 5],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'V')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')

    return puzzle
