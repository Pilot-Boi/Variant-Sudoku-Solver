"""PuzzleMadness X/V Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 8, 0, 0, 7, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'V')
    puzzle.add_xv((1, 6), (1, 7), 'V')
    puzzle.add_xv((3, 6), (3, 7), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'V')
    puzzle.add_xv((6, 6), (7, 6), 'X')

    return puzzle
