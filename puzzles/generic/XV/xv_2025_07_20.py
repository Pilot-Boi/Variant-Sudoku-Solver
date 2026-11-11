"""PuzzleMadness X/V Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'X')

    return puzzle
