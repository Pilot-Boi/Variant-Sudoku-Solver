"""PuzzleMadness X/V Sudoku — 2025-06-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-06-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/6/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((7, 1), (7, 2), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
