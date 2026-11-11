"""PuzzleMadness X/V Sudoku — 2025-09-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 8, 0, 0, 0, 0, 6, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')

    return puzzle
