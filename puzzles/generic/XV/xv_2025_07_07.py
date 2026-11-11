"""PuzzleMadness X/V Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [4, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 0), (2, 1), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 4), (2, 5), 'V')
    puzzle.add_xv((2, 5), (2, 6), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((7, 2), (7, 3), 'V')
    puzzle.add_xv((7, 3), (7, 4), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 7), (8, 8), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((5, 2), (6, 2), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')

    return puzzle
