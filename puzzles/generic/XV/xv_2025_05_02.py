"""PuzzleMadness X/V Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 3],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((1, 2), (1, 3), 'X')
    puzzle.add_xv((2, 2), (2, 3), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'V')
    puzzle.add_xv((3, 3), (3, 4), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'V')
    puzzle.add_xv((0, 1), (1, 1), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 2), (3, 2), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'V')
    puzzle.add_xv((2, 6), (3, 6), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 2), (4, 2), 'V')
    puzzle.add_xv((3, 5), (4, 5), 'X')
    puzzle.add_xv((4, 0), (5, 0), 'V')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
