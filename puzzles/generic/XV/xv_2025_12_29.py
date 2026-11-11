"""PuzzleMadness X/V Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
