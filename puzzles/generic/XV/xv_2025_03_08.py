"""PuzzleMadness X/V Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((1, 5), (1, 6), 'V')
    puzzle.add_xv((1, 7), (1, 8), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 7), (3, 8), 'V')
    puzzle.add_xv((4, 2), (4, 3), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((6, 7), (6, 8), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 2), (1, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
