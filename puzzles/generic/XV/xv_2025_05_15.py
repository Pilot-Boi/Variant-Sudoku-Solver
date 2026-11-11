"""PuzzleMadness X/V Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 8, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 3],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((0, 1), (0, 2), 'X')
    puzzle.add_xv((3, 1), (3, 2), 'X')
    puzzle.add_xv((3, 3), (3, 4), 'V')
    puzzle.add_xv((4, 1), (4, 2), 'V')
    puzzle.add_xv((5, 7), (5, 8), 'V')
    puzzle.add_xv((7, 6), (7, 7), 'V')
    puzzle.add_xv((8, 0), (8, 1), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'V')
    puzzle.add_xv((8, 5), (8, 6), 'X')
    puzzle.add_xv((0, 5), (1, 5), 'X')
    puzzle.add_xv((0, 7), (1, 7), 'V')
    puzzle.add_xv((2, 1), (3, 1), 'X')
    puzzle.add_xv((2, 3), (3, 3), 'X')
    puzzle.add_xv((4, 1), (5, 1), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((4, 3), (5, 3), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((6, 6), (7, 6), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')

    return puzzle
