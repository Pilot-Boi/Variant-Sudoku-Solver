"""PuzzleMadness X/V Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 7, 0, 0],
        [0, 9, 0, 6, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((1, 0), (1, 1), 'X')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 7), (4, 8), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'V')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
