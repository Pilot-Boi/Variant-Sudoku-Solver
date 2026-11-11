"""PuzzleMadness Thermometer Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 6, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 3, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 2), (1, 2), (1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (4, 5)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3), (6, 3), (6, 2)])
    puzzle.add_thermometer([(2, 4), (2, 5), (2, 6), (1, 6), (1, 5)])
    puzzle.add_thermometer([(5, 8), (4, 8), (4, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(4, 1), (5, 1), (6, 1), (6, 0), (5, 0)])
    puzzle.add_thermometer([(6, 4), (6, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(7, 7), (7, 6), (7, 5), (7, 4)])
    puzzle.add_thermometer([(1, 8), (0, 8), (0, 7), (1, 7)])
    puzzle.add_thermometer([(6, 6), (6, 7), (6, 8)])
    puzzle.add_thermometer([(3, 7), (3, 8), (2, 8)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(3, 1), (3, 2), (4, 2)])
    puzzle.add_thermometer([(0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])

    return puzzle
