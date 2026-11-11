"""PuzzleMadness X/V Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'V')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((2, 7), (2, 8), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'V')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'V')

    return puzzle
