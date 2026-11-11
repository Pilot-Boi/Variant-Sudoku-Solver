"""PuzzleMadness X/V Sudoku — 2025-02-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 1, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 2, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
