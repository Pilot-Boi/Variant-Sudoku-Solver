"""PuzzleMadness X/V Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
