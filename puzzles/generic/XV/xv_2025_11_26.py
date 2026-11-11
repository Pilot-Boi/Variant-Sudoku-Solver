"""PuzzleMadness X/V Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 2, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [2, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
