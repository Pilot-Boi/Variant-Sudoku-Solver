"""PuzzleMadness X/V Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [7, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((4, 3), (4, 4), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((0, 8), (1, 8), 'V')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((3, 6), (4, 6), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 4), (5, 4), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
