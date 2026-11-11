"""PuzzleMadness X/V Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [3, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 4), (0, 5), 'X')
    puzzle.add_xv((1, 4), (1, 5), 'X')
    puzzle.add_xv((1, 6), (1, 7), 'X')
    puzzle.add_xv((4, 0), (4, 1), 'X')
    puzzle.add_xv((4, 4), (4, 5), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'X')
    puzzle.add_xv((5, 6), (5, 7), 'V')
    puzzle.add_xv((6, 4), (6, 5), 'X')
    puzzle.add_xv((6, 6), (6, 7), 'X')
    puzzle.add_xv((8, 3), (8, 4), 'X')
    puzzle.add_xv((1, 3), (2, 3), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((5, 7), (6, 7), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((7, 1), (8, 1), 'X')
    puzzle.add_xv((7, 2), (8, 2), 'X')
    puzzle.add_xv((7, 5), (8, 5), 'X')

    return puzzle
