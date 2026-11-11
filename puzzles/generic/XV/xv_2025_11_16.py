"""PuzzleMadness X/V Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 9, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
