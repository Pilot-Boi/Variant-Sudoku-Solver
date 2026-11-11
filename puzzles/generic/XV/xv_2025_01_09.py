"""PuzzleMadness X/V Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 3), (1, 4), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'V')
    puzzle.add_xv((3, 4), (3, 5), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'V')
    puzzle.add_xv((5, 0), (5, 1), 'X')
    puzzle.add_xv((5, 1), (5, 2), 'V')
    puzzle.add_xv((5, 4), (5, 5), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'X')
    puzzle.add_xv((1, 8), (2, 8), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'X')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 1), (4, 1), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 5), (6, 5), 'V')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
