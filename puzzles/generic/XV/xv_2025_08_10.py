"""PuzzleMadness X/V Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'X/V Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/sudokuxv/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 9, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_xv((2, 3), (2, 4), 'X')
    puzzle.add_xv((2, 6), (2, 7), 'V')
    puzzle.add_xv((4, 3), (4, 4), 'V')
    puzzle.add_xv((4, 5), (4, 6), 'X')
    puzzle.add_xv((4, 6), (4, 7), 'V')
    puzzle.add_xv((5, 2), (5, 3), 'V')
    puzzle.add_xv((6, 2), (6, 3), 'X')
    puzzle.add_xv((7, 5), (7, 6), 'X')
    puzzle.add_xv((8, 1), (8, 2), 'X')
    puzzle.add_xv((8, 4), (8, 5), 'X')
    puzzle.add_xv((1, 5), (2, 5), 'X')
    puzzle.add_xv((1, 6), (2, 6), 'X')
    puzzle.add_xv((3, 4), (4, 4), 'X')
    puzzle.add_xv((4, 2), (5, 2), 'X')
    puzzle.add_xv((6, 1), (7, 1), 'X')
    puzzle.add_xv((6, 3), (7, 3), 'X')
    puzzle.add_xv((6, 5), (7, 5), 'X')
    puzzle.add_xv((7, 7), (8, 7), 'X')
    puzzle.add_xv((7, 8), (8, 8), 'V')

    return puzzle
