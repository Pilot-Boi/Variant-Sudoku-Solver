"""PuzzleMadness X/V Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 0, 8, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 3), (0, 4), 'X')
    puzzle.add_xv((2, 0), (2, 1), 'V')
    puzzle.add_xv((2, 2), (2, 3), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((5, 0), (5, 1), 'V')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'X')
    puzzle.add_xv((1, 4), (2, 4), 'X')
    puzzle.add_xv((2, 0), (3, 0), 'X')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((4, 2), (5, 2), 'V')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((6, 4), (7, 4), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'V')
    puzzle.add_xv((7, 4), (8, 4), 'V')
    puzzle.add_xv((7, 7), (8, 7), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'X')

    return puzzle
