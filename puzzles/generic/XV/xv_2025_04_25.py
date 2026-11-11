"""PuzzleMadness X/V Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 2, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'V')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'X')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')

    return puzzle
