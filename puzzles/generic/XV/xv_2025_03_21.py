"""PuzzleMadness X/V Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((7, 2), (8, 2), 'X')

    return puzzle
