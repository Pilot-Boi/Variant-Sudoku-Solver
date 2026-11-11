"""PuzzleMadness X/V Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((4, 1), (4, 2), 'X')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 7), (4, 8), 'X')
    puzzle.add_xv((5, 4), (5, 5), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 3), (6, 4), 'X')
    puzzle.add_xv((6, 5), (6, 6), 'X')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((8, 6), (8, 7), 'V')
    puzzle.add_xv((0, 2), (1, 2), 'V')
    puzzle.add_xv((0, 4), (1, 4), 'X')
    puzzle.add_xv((1, 0), (2, 0), 'V')
    puzzle.add_xv((1, 4), (2, 4), 'V')
    puzzle.add_xv((1, 7), (2, 7), 'X')
    puzzle.add_xv((3, 0), (4, 0), 'V')
    puzzle.add_xv((3, 1), (4, 1), 'V')
    puzzle.add_xv((3, 3), (4, 3), 'X')
    puzzle.add_xv((4, 6), (5, 6), 'X')
    puzzle.add_xv((5, 4), (6, 4), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'V')
    puzzle.add_xv((5, 8), (6, 8), 'V')
    puzzle.add_xv((6, 2), (7, 2), 'V')
    puzzle.add_xv((7, 1), (8, 1), 'V')

    return puzzle
