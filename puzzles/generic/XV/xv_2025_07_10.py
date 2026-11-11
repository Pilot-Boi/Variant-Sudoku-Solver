"""PuzzleMadness X/V Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 8, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 3, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [3, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((1, 2), (1, 3), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'X')

    return puzzle
