"""PuzzleMadness X/V Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 0), (0, 1), 'X')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((5, 3), (5, 4), 'V')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 4), (3, 4), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((5, 3), (6, 3), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 6), (8, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
