"""PuzzleMadness X/V Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
