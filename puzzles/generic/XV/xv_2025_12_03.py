"""PuzzleMadness X/V Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 0, 0],
        [0, 0, 0, 0, 9, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
