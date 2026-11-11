"""PuzzleMadness X/V Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 5, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 2), (0, 3), 'V')
    puzzle.add_xv((0, 6), (0, 7), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'V')
    puzzle.add_xv((5, 6), (5, 7), 'X')
    puzzle.add_xv((0, 3), (1, 3), 'V')
    puzzle.add_xv((1, 2), (2, 2), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((2, 6), (3, 6), 'V')
    puzzle.add_xv((2, 7), (3, 7), 'V')
    puzzle.add_xv((2, 8), (3, 8), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 8), (5, 8), 'X')
    puzzle.add_xv((5, 0), (6, 0), 'V')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 7), (6, 7), 'V')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((6, 7), (7, 7), 'X')

    return puzzle
