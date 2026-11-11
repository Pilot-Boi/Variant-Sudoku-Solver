"""PuzzleMadness X/V Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((0, 4), (0, 5), 'V')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 1), (2, 2), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'V')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'V')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
