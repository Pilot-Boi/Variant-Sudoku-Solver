"""PuzzleMadness X/V Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 4), (2, 5), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 5), (3, 6), 'X')
    puzzle.add_xv((3, 7), (3, 8), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'X')
    puzzle.add_xv((2, 5), (3, 5), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 2), (7, 2), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((6, 8), (7, 8), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'V')

    return puzzle
