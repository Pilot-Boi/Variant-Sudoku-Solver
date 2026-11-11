"""PuzzleMadness X/V Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 7, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((0, 7), (0, 8), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'V')
    puzzle.add_xv((3, 0), (3, 1), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'V')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'V')
    puzzle.add_xv((7, 3), (8, 3), 'X')

    return puzzle
