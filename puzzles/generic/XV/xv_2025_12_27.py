"""PuzzleMadness X/V Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
