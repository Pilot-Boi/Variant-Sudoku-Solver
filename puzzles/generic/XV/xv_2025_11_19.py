"""PuzzleMadness X/V Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 1), (2, 2), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'X')
    puzzle.add_xv((3, 2), (3, 3), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((5, 5), (5, 6), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 2), (8, 3), 'V')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 0), (1, 0), 'X')
    puzzle.add_xv((0, 4), (1, 4), 'V')
    puzzle.add_xv((0, 5), (1, 5), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'V')

    return puzzle
