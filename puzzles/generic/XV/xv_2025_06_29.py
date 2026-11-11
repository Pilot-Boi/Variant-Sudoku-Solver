"""PuzzleMadness X/V Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
