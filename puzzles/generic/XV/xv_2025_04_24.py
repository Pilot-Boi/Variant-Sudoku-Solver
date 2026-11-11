"""PuzzleMadness X/V Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
