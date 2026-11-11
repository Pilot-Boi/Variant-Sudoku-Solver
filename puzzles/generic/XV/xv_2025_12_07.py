"""PuzzleMadness X/V Sudoku — 2025-12-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-12-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/12/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 1), (1, 2), 'V')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'X')

    return puzzle
