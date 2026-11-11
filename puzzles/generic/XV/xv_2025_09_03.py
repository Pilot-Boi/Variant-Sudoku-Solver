"""PuzzleMadness X/V Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 8, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'V')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')

    return puzzle
