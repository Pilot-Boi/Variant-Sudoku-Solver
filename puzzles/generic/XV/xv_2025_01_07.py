"""PuzzleMadness X/V Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 6],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((6, 0), (6, 1), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'V')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'X')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
