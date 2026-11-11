"""PuzzleMadness X/V Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 7, 0, 0, 8],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((7, 1), (7, 2), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 0), (7, 0), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'V')

    return puzzle
