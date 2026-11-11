"""PuzzleMadness X/V Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 1), (1, 2), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 0), (3, 1), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')

    return puzzle
