"""PuzzleMadness X/V Sudoku — 2025-03-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-03-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/3/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 1, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 3), (0, 4), 'V')
    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'V')
    puzzle.add_xv((0, 0), (1, 0), 'V')
    puzzle.add_xv((1, 1), (2, 1), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'V')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((6, 1), (7, 1), 'V')
    puzzle.add_xv((7, 6), (8, 6), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
