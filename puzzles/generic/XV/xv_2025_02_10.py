"""PuzzleMadness X/V Sudoku — 2025-02-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 1],
        [0, 3, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((6, 1), (6, 2), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
