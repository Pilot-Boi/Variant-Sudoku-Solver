"""PuzzleMadness X/V Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
