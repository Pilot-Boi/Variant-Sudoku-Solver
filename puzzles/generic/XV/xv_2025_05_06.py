"""PuzzleMadness X/V Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 7), (2, 8), 'X')
    puzzle.add_xv((5, 2), (5, 3), 'X')
    puzzle.add_xv((6, 2), (6, 3), 'V')
    puzzle.add_xv((6, 5), (6, 6), 'V')
    puzzle.add_xv((7, 0), (7, 1), 'X')
    puzzle.add_xv((7, 4), (7, 5), 'X')
    puzzle.add_xv((7, 7), (7, 8), 'X')
    puzzle.add_xv((0, 6), (1, 6), 'V')
    puzzle.add_xv((0, 7), (1, 7), 'X')
    puzzle.add_xv((1, 1), (2, 1), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 7), (4, 7), 'V')
    puzzle.add_xv((3, 8), (4, 8), 'V')
    puzzle.add_xv((4, 1), (5, 1), 'V')
    puzzle.add_xv((4, 5), (5, 5), 'X')
    puzzle.add_xv((4, 7), (5, 7), 'X')
    puzzle.add_xv((5, 1), (6, 1), 'X')
    puzzle.add_xv((5, 6), (6, 6), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'V')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
