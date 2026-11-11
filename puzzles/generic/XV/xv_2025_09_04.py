"""PuzzleMadness X/V Sudoku — 2025-09-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [7, 0, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'V')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 0), (8, 0), 'X')
    puzzle.add_xv((7, 3), (8, 3), 'V')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
