"""PuzzleMadness X/V Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 5), (0, 6), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 4), (7, 4), 'V')

    return puzzle
