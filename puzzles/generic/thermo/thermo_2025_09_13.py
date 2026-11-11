"""PuzzleMadness Thermometer Sudoku — 2025-09-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 4, 0, 1],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 4],
        [0, 6, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 6), (2, 6), (2, 5), (2, 4), (2, 3), (3, 3)])
    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3), (8, 3), (8, 4), (7, 4)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2), (1, 2), (2, 2)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 7), (4, 7), (4, 8)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(8, 7), (7, 7), (7, 6), (8, 6)])
    puzzle.add_thermometer([(2, 0), (2, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(6, 2), (5, 2), (4, 2), (4, 3)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
