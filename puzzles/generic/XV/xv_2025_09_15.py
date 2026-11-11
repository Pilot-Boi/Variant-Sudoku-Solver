"""PuzzleMadness X/V Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
